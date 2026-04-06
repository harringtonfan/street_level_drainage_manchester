import sys
from pathlib import Path

# Ensure the repository root is on the Python path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely import wkt
from shapely.geometry import box


def main() -> None:
    # Read matched CSV produced by the repository workflow
    df = pd.read_csv("matched_data/manchester_usrn_soil.csv")
    df["geometry"] = df["geometry"].apply(wkt.loads)
    gdf = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:27700")

    # Keep impeded drainage segments only
    gdf_impeded = gdf[gdf["DRAINAGE"] == "Impeded drainage"].copy()

    # Read original soil polygons for background layer
    soil = gpd.read_file("input_data/NationalSoilMap.gpkg")

    # Expanded Manchester bbox (Option A)
    xmin, ymin, xmax, ymax = 366000, 378000, 404000, 407000
    bbox = gpd.GeoDataFrame(
        geometry=[box(xmin, ymin, xmax, ymax)],
        crs="EPSG:27700"
    )

    soil_clip = gpd.clip(soil, bbox)
    soil_impeded = soil_clip[soil_clip["DRAINAGE"] == "Impeded drainage"].copy()

    # Plot
    fig, ax = plt.subplots(figsize=(20, 12))

    soil_impeded.plot(
    ax=ax,
    color="#cfdfef",
    edgecolor="none",
    alpha=0.58,
    zorder=1
)

    gdf_impeded.plot(
    ax=ax,
    color="#1f5fa8",
    linewidth=0.68,
    alpha=1.0,
    zorder=2
)

    xmin, ymin, xmax, ymax = gdf_impeded.total_bounds
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    ctx.add_basemap(
    ax,
    crs=gdf_impeded.crs,
    source=ctx.providers.CartoDB.Positron,
    attribution=False,
    zoom=12,
    zorder=0
)

    ax.text(
    0.012,
    0.990,
    "Street-Level Impeded Drainage in Manchester",
    transform=ax.transAxes,
    fontsize=13,
    fontweight="bold",
    ha="left",
    va="top",
    color="black",
    zorder=10
)

    # Put attribution INSIDE the map, lower-left corner
    ax.text(
        0.001,
        0.003,
        "Contains OS data © Crown copyright and database right 2026.\n"
        "Contains LandIS® Portal NATMAP data © Cranfield University 2026, "
        "subject to the LandIS Portal Open Licence.",
        transform=ax.transAxes,
        fontsize=6,
        color="black",
        ha="left",
        va="bottom",
        zorder=10
    )

    ax.set_axis_off()
    plt.tight_layout()

    # Save standard PNG
    plt.savefig(
        "matched_data/manchester_impeded_drainage_final.png",
        dpi=300,
        bbox_inches="tight",
        facecolor="white"
    )

    # Save high-resolution PNG
    plt.savefig(
        "matched_data/manchester_impeded_drainage_final_highres.png",
        dpi=600,
        bbox_inches="tight",
        facecolor="white"
    )

    # Save vector PDF
    plt.savefig(
        "matched_data/manchester_impeded_drainage_final.pdf",
        bbox_inches="tight",
        facecolor="white"
    )

    plt.show()


if __name__ == "__main__":
    main()