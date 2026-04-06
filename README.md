# Street-Level Impeded Drainage in Manchester

This project links OS Open USRN street segments to National Soil Map soil drainage attributes in order to identify and map parts of Manchester’s road network associated with impeded drainage conditions.

![Manchester impeded drainage map](manchester_impeded_drainage_preview.png)

## Project Question

Which parts of Manchester’s road network are located in areas with impeded drainage conditions, and how might this matter for infrastructure planning and maintenance?

## Overview

Environmental constraints are often stored as polygon layers, while transport and infrastructure systems are usually managed through network-based identifiers. This project connects those two spatial logics by matching USRN street segments to soil polygons and producing a street-level map of impeded drainage conditions in Manchester.

The project uses the `usrn-matcher` workflow as its matching backbone, then applies that workflow to Manchester and reconstructs the mapped output as a standalone case study.

## Study Area

Manchester, using a Manchester-area bounding box within the workflow.

## Data

- **OS Open USRN** — street-segment identifiers and line geometries
- **National Soil Map** — polygon-based soil and drainage attributes

Raw input data is not stored in this repository. Place the required GeoPackage files in `input_data/` before running the workflow.

## Workflow

1. Read OS Open USRN and National Soil Map GeoPackage files.
2. Apply a Manchester bounding box to define the study area.
3. Match street segments to soil polygons using the repository workflow.
4. Export matched output as a CSV with geometry and soil attributes.
5. Rebuild the matched geometries and generate a final mapped output focused on **Impeded drainage**.

## Repository Structure

```text
usrn-matcher/
├── input_data/                      # local input GeoPackage files (not tracked)
├── matched_data/                    # matched outputs and final figures
├── output_data/                     # cached parquet outputs from the workflow
├── scripts/                         # Manchester-specific scripts
├── usrn_soil_matcher/               # core repository matching code
├── README.md
└── pyproject.toml
```

## Key Files

- `scripts/run_match_manchester.py`  
  Runs the Manchester matching workflow and writes the matched CSV.

- `scripts/make_manchester_map.py`  
  Reads the matched output and generates the final Manchester map.

- `matched_data/manchester_usrn_soil.csv`  
  Street-segment-level matched output from the workflow.

- `matched_data/manchester_impeded_drainage_final.png`  
  Standard PNG export of the final figure.

- `matched_data/manchester_impeded_drainage_final_highres.png`  
  High-resolution PNG export of the final figure.

- `matched_data/manchester_impeded_drainage_final.pdf`  
  Vector PDF export of the final figure.

- `manchester_impeded_drainage_preview.png`  
  Preview image used in the repository homepage.

## Outputs

This repository currently includes:

- a matched street-segment dataset for Manchester
- a standard PNG export
- a high-resolution PNG export
- a PDF export of the final figure

## Quick Start

Run the Manchester match:

```bash
python scripts/run_match_manchester.py
```

Generate the final map:

```bash
python scripts/make_manchester_map.py
```

## Why It Matters

Street networks are often the practical unit through which infrastructure is managed, while environmental data is often published as area-based polygon layers. This project shows how polygon-based drainage information can be translated into street-segment-level outputs that are easier to inspect, map, and potentially use in infrastructure-oriented analysis.

From a public policy perspective, this kind of workflow can help identify where environmental constraints overlap with everyday infrastructure, making it easier to think about road maintenance, local planning, and uneven physical vulnerability across urban space.

## Notes

This is a Manchester adaptation built on top of the repository’s matching workflow. The final map, project framing, and Manchester-specific application were developed as part of this case study.

## Sources and Acknowledgments

This project uses:

- **OS Open USRN**
- **National Soil Map / LandIS Portal NATMAP data**

The spatial matching workflow is based on the `usrn-matcher` repository. This project adapts that workflow to Manchester and develops a separate mapped output and project presentation around that result.