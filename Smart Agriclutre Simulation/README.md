# Smart Agriculture Quality Evaluation

This project simulates quality improvements in a smart agriculture environment using machine learning–based weighting of IoT performance indicators.

## 📁 Project Structure

- `data/agriculture_simulation_data.csv` — Synthetic dataset representing sensor behavior and network performance
- `quality_agriculture.py` — Python script for computing weighted quality scores and visualizing improvements
- `results/agriculture_results.txt` — Output file with paired t-test and Cohen's d results
- `results/agriculture_quality_distribution.png` — Bar chart comparing baseline and weighted scores
- `requirements.txt` — Python dependencies required to run the script

## ⚙️ How to Use

1. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the analysis script:
   ```bash
   python quality_agriculture.py
   ```

3. View results in the `results/` folder:
   - Statistical summary in `agriculture_results.txt`
   - Visualization in `agriculture_quality_distribution.png`

*📊 Notes*

- The simulation focuses on three key indicators: `latency`, `sensor_accuracy`, and `fault_recovery`
- Weights are derived using Random Forest regression based on SLA relevance
- Results align with Table IV and Section IV of the original research study

