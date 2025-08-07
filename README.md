# IoT Quality Framework

This repository contains two experimental pipelines for evaluating quality improvements in IoT environments using machine learning–based metric weighting.

## 1. Smart Agriculture Simulation

This experiment simulates a smart farming scenario using synthetic sensor data. It applies Random Forest regression to assign weights to key performance indicators and evaluates the impact on overall quality scores.

Folder: Smart agriculture simulation

Contents:
- data/agriculture_simulation_data.csv
- quality_agriculture.py
- results/agriculture_results.txt
- results/agriculture_quality_distribution.png
- requirements.txt
- README.md

## 2. Smart Industrial Quality Evaluation

This experiment validates the framework using real-world data from the ToN-IoT dataset. It compares baseline performance metrics with weighted quality scores across industrial environments.

Folder: Smart industrial quality evaluation

Contents:
- data/industrial_quality_data.csv
- quality_industrial.py
- results/industrial_results.txt
- results/industrial_quality_distribution.png
- requirements.txt
- README.md

## How to Run

Each experiment is self-contained. Navigate into the desired folder and follow the instructions in its README.md file.

## License

You may include a license file here if you plan to share or publish the project.
