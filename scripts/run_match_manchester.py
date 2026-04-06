import sys
from pathlib import Path

# Ensure the repository root is on the Python path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from usrn_soil_matcher import UsrnSoilMatcher


def main() -> None:
    matcher = UsrnSoilMatcher.from_gpkgs(
        usrn_gpkg="input_data/osopenusrn.gpkg",
        soil_gpkg="input_data/NationalSoilMap.gpkg",
    )

    # Expanded Manchester bbox (Option A)
    manchester_bbox = [366000, 378000, 404000, 407000]

    table = matcher.match(bbox=manchester_bbox)
    matcher.to_csv(table, "matched_data/manchester_usrn_soil.csv")


if __name__ == "__main__":
    main()