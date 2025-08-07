# Smart Industrial Quality Evaluation

This project analyzes performance improvements in industrial IoT environments using weighted quality scores derived from ToN-IoT dataset metrics.

## 📁 Project Structure

- `data/industrial_quality_data.csv` — Input dataset with 30 records across Smart Home, Smart Office, and Smart Factory environments
- `quality_industrial.py` — Python script for statistical analysis and visualization
- `results/industrial_results.txt` — Output file containing paired t-test and Cohen's d results
- `results/industrial_quality_distribution.png` — Bar chart comparing baseline and weighted scores
- `requirements.txt` — Python dependencies required to run the script

## ⚙️ How to Use

1. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the analysis script:
   ```bash
   python quality_industrial.py
   ```

3. View results in the `results/` folder:
   - Statistical summary in `industrial_results.txt`
   - Visualization in `industrial_quality_distribution.png`

*📊 Notes*

- The analysis focuses on four key metrics: `latency`, `uptime`, `fault_recovery`, and `sla_violations`
- `cpu_usage` was mentioned in the study but excluded from final statistical evaluation
- Data and methodology align with Table V and Section IV of the original research study
