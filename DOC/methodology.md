# Methodology

This project aims to evaluate the quality of IoT systems in two domains: Smart Agriculture and Smart Industrial environments. The methodology combines simulation data, machine learning, and statistical analysis to assess service-level performance.

## 1. Data Collection

- Smart Agriculture: Simulated data includes latency, sensor accuracy, and fault recovery metrics.
- Smart Industry: Real-world data from the ToN-IoT dataset, focusing on industrial sensors and network behavior.

## 2. Feature Selection

Key indicators were selected based on domain relevance:
- Latency
- Sensor Accuracy
- Fault Recovery

These features are used to predict SLA (Service Level Agreement) scores.

## 3. Model Training

A Random Forest Regressor is trained to learn the relationship between indicators and SLA scores. Feature importances are extracted to compute weighted quality scores.

## 4. Quality Evaluation

- Baseline Score: Original SLA score without weighting
- Weighted Score: SLA score adjusted using learned feature weights

## 5. Statistical Analysis

A paired t-test is used to compare baseline and weighted scores. Cohen's d is calculated to measure effect size.

## 6. Visualization

Bar charts are generated to compare average quality scores between baseline and weighted evaluations.

## 7. Output

Results are saved in:
- `results/agriculture_results.txt`
- `results/industrial_results.txt`
- Corresponding PNG charts for visual comparison

## Conclusion

This framework provides a scalable and data-driven approach to evaluating IoT system quality across different domains. It can be extended to other sectors with minimal adjustments.

