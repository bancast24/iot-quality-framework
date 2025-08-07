# IoT Quality Framework

This repository contains two experimental pipelines for evaluating quality improvements in IoT environments using machine learning–based metric weighting.

## 1. Smart Agriculture Simulation

Simulates a smart farming scenario using synthetic sensor data. Applies Random Forest regression to assign weights to key performance indicators and evaluates the impact on overall quality scores.

Folder: `Smart Agriculture Simulation`

Contents:
`data/agriculture_simulation_data.csv`
- `quality_agriculture.py`
- `results/agriculture_results.txt`
  `results/agriculture_quality_distribution.png`
- `requirements.txt`
- `README.md`

## 2. Smart Industrial Quality Evaluation

Validates the framework using real-world data from the ToN-IoT dataset. Compares baseline performance metrics with weighted quality scores across industrial environments.

Folder: `Smart Industrial Quality Evaluation`

Contents:
- `data/industrial_quality_data.csv`
- `quality_industrail.py`
- `results/industrial_results.txt`
- `results/industrial_quality_distribution.png`
- `requirements.txt`
- `README.md`

## How to Run with Docker

You can run either experiment using Docker and the unified `main.py` controller.

### 1. Build the Docker image

docker-compose build

2. Run Agriculture Simulation

docker-compose up

(Default command runs agriculture simulation. To change, edit `command:` in `docker-compose.yml`)

3. Run Industrial Simulation

Edit `docker-compose.yml`:

command: python main.py industrial

Then run:

docker-compose up

Manual Run (Without Docker)

You can also run each experiment manually:

python main.py agriculture
python main.py industrial


License

This project is licensed under the MIT License. See the `LICENSE` file for details.
