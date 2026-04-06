# Linking Environmental Constraints to Street-Level Infrastructure: A Manchester Case Study

This project translates polygon-based environmental data into street-segment-level infrastructure information by linking **OS Open USRN** street segments to **National Soil Map** drainage attributes. Using Manchester as a case study, the project identifies parts of the road network associated with **impeded drainage** conditions and presents the output as a street-level map relevant to infrastructure planning and policy analysis.

![Manchester impeded drainage map](manchester_impeded_drainage_preview.png)

## Project Question

Which parts of Manchester’s road network intersect impeded drainage conditions, and how can this kind of street-level spatial attribution support infrastructure planning and policy analysis?

## Overview

Environmental constraints are often stored as polygon layers, while infrastructure systems are more often managed through network-based identifiers such as road segments or street references. This creates a practical mismatch between how environmental information is published and how infrastructure is often understood or managed.

This project addresses that mismatch by spatially matching **USRN street segments** to **soil polygons** and producing a street-level output for Manchester. The result is a mapped representation of where impeded drainage conditions overlap with the road network, showing how area-based environmental data can be translated into more decision-relevant infrastructure indicators.

The project uses the `usrn-matcher` workflow as its technical backbone, then adapts that workflow to Manchester and reframes the result as a standalone policy-relevant geospatial case study.

## Why This Project

What interested me in this project was not only the map itself, but the broader workflow problem behind it: how to turn complex, heterogeneous spatial data into outputs that are easier to interpret, communicate, and potentially use in planning or maintenance contexts.

In that sense, the project is less about a single map and more about a reproducible method for transforming raw geospatial information into street-level indicators.

## Study Area

Manchester, using a Manchester-area bounding box within the workflow.

## Data

- **OS Open USRN** — street-segment identifiers and line geometries
- **National Soil Map** — polygon-based soil and drainage attributes

Raw input data is not stored in this repository. Place the required GeoPackage files in `input_data/` before running the workflow.

## Workflow

1. Read **OS Open USRN** and **National Soil Map** GeoPackage files.
2. Apply a Manchester bounding box to define the study area.
3. Match street segments to soil polygons using the repository workflow.
4. Export matched output as a CSV with geometry and soil attributes.
5. Rebuild the matched geometries and generate a final mapped output focused on **Impeded drainage**.

## Repository Structure

```text
street_level_drainage_manchester/
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

Street networks are often the practical unit through which infrastructure is maintained and interpreted, while environmental information is often distributed as area-based polygon data. This project shows how those two spatial logics can be connected in a way that produces interpretable, street-level outputs.

From a public policy perspective, this kind of workflow can help identify where environmental constraints overlap with everyday infrastructure, making it easier to think about questions of road maintenance, local planning, and uneven physical vulnerability across urban space.

More broadly, the project reflects an interest in building workflows that make complex spatial information more legible and more usable for applied analysis.

## What the Map Shows

The map shows that impeded drainage conditions are not evenly distributed across Manchester’s road network. Instead, they appear in spatially concentrated clusters, with some parts of the network intersecting these conditions much more heavily than others.

This matters for two reasons. First, it shows that a polygon-based environmental layer can be translated into a street-segment-level infrastructure indicator. Second, it suggests that physical environmental constraints are not distributed uniformly across urban space, but overlap with specific parts of the road network in ways that could be more relevant for planning, maintenance, or further investigation.

The map should be read as an indicator of spatial overlap, not as proof of road damage or infrastructure failure. Its main contribution is to identify where impeded drainage conditions and the street network coincide, and to make that overlap easier to interpret at the street level.

## Notes

This is a Manchester adaptation built on top of the repository’s matching workflow. The final map, project framing, and Manchester-specific application were developed as part of this case study.

## Sources and Acknowledgments

This project uses:

- **OS Open USRN**
- **National Soil Map / LandIS Portal NATMAP data**

The spatial matching workflow is based on the `usrn-matcher` repository. This project adapts that workflow to Manchester and develops a separate mapped output and project presentation around that result.