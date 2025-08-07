# Project Overview

## Title: IoT Quality Evaluation Framework

This project implements a validated, context-aware framework for evaluating the quality of IoT systems across multiple operational domains. It integrates simulation data, machine learning, and statistical analysis to assess service-level performance in both synthetic and real-world environments.


## Objectives

- Apply a multidomain evaluation model to IoT systems
- Use classified quality indicators and learned weights to compute SLA-based quality scores
- Validate the framework through agricultural simulation and industrial data analysis
- Quantify improvements using statistical significance and effect size


## Domains Covered

The framework evaluates five operational domains:
- Device-level performance
- Network behavior
- Environmental monitoring
- Sensor data integrity
- Service delivery quality


## Structure

### 🔹 Main Directory
- `main.py`: Executes both experiments
- `README.md`: General documentation
- `CHANGELOG.md`: Version history
- `LICENSE`: Usage terms
- `.gitignore`: Git configuration

### 🔹 Experiments
- `Smart Agriculture Simulation/`
  - `quality_agriculture.py`
  - `data/`
  - `results/`
- `Smart Industrial Quality Evaluation/`
  - `quality_industrial.py`
  - `data/`
  - `results/`

### 🔹 Documentation
- `DOC/methodology.md`: Analytical process
- `DOC/overview.md`: This file
- `DOC/references.md`: Source materials


## Technologies Used

- Python 3.x
- Pandas, NumPy, Matplotlib
- Scikit-learn (Random Forest)
- SciPy (Statistical tests)


## Evaluation & Results

- Smart Agriculture Simulation
  Quality improved by 16% using weighted indicators
  p = 0.0003, Cohen’s d = 1.84

- Smart Industrial Evaluation
  Quality improved by 12% using weighted indicators
  p = 0.00001, Cohen’s d = 1.76

Outputs include:
- `.txt` files with statistical results
- `.png` charts comparing baseline vs weighted scores


## Future Work

- Extend to smart healthcare, smart cities, and other IoT domains
- Integrate real-time data streams and anomaly detection
- Explore federated learning and Quality 4.0 models
- Enhance context-awareness and adaptive evaluation


## Author

This framework was developed to advance the reliability and performance of IoT systems through data-driven, domain-specific quality evaluation.
