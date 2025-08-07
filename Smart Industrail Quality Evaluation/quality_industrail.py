import pandas as pd
from scipy.stats import ttest_rel
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_csv("industrial_quality_data.csv")

# Ensure the results directory exists
os.makedirs("results", exist_ok=True)

# Filter data by environment
home = df[df["environment"] == "Smart Home"]
office = df[df["environment"] == "Smart Office"]
factory = df[df["environment"] == "Smart Factory"]

# Compute baseline scores for each indicator in each environment
baseline_scores = [
    home["latency"].mean(),
    home["uptime"].mean(),
    home["fault_recovery"].mean(),
    home["sla_violations"].mean(),
    office["latency"].mean(),
    office["uptime"].mean(),
    office["fault_recovery"].mean(),
    office["sla_violations"].mean(),
    factory["latency"].mean(),
    factory["uptime"].mean(),
    factory["fault_recovery"].mean(),
    factory["sla_violations"].mean()
]

# Use the average quality score as the weighted score for all indicators
weighted_scores = [
    home["quality_score"].mean(),
    home["quality_score"].mean(),
    home["quality_score"].mean(),
    home["quality_score"].mean(),
    office["quality_score"].mean(),
    office["quality_score"].mean(),
    office["quality_score"].mean(),
    office["quality_score"].mean(),
    factory["quality_score"].mean(),
    factory["quality_score"].mean(),
    factory["quality_score"].mean(),
    factory["quality_score"].mean()
]

# Perform paired t-test
t_stat, p_value = ttest_rel(weighted_scores, baseline_scores)

# Calculate Cohen's d effect size
diff = pd.Series(weighted_scores) - pd.Series(baseline_scores)
cohen_d = diff.mean() / diff.std()

# Save statistical results to a text file
with open("results/industrial_results.txt", "w") as f:
    f.write(f"Paired t-test: t={t_stat:.3f}, p={p_value:.5f}\n")
    f.write(f"Cohen's d: {cohen_d:.2f}\n")

# Create bar chart comparing baseline and weighted scores
labels = [
    "Latency (Home)", "Uptime (Home)", "Recovery (Home)", "SLA (Home)",
    "Latency (Office)", "Uptime (Office)", "Recovery (Office)", "SLA (Office)",
    "Latency (Factory)", "Uptime (Factory)", "Recovery (Factory)", "SLA (Factory)"
]

x = range(len(labels))
plt.figure(figsize=(12, 6))
plt.bar(x, baseline_scores, width=0.4, label="Baseline", align="center")
plt.bar([i + 0.4 for i in x], weighted_scores, width=0.4, label="Weighted", align="center")
plt.xticks([i + 0.2 for i in x], labels, rotation=45, ha="right")
plt.ylabel("Score")
plt.title("Quality Score Comparison Across ToN-IoT Environments")
plt.legend()
plt.tight_layout()
plt.savefig("results/industrial_quality_distribution.png")
