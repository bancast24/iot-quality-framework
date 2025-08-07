import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from scipy.stats import ttest_rel

# Load data
df = pd.read_csv("data/agriculture_simulation_data.csv")

# Select relevant indicators
indicators = ["latency", "sensor_accuracy", "fault_recovery"]
X = df[indicators]
y = df["sla_score"]

# Train model to get weights
model = RandomForestRegressor()
model.fit(X, y)
weights = model.feature_importances_

# Compute weighted quality scores
df["weighted_score"] = np.dot(X, weights)

# Statistical comparison
t_stat, p_value = ttest_rel(df["baseline_score"], df["weighted_score"])
mean_diff = df["weighted_score"].mean() - df["baseline_score"].mean()
cohen_d = mean_diff / df["baseline_score"].std()

# Save results
with open("results/agriculture_results.txt", "w") as f:
    f.write(f"Paired t-test: t={t_stat:.3f}, p={p_value:.5f}\n")
    f.write(f"Cohen's d: {cohen_d:.2f}\n")

# Plot comparison
plt.figure(figsize=(8, 5))
plt.bar(["Baseline", "Weighted"], [df["baseline_score"].mean(), df["weighted_score"].mean()], color=["gray", "green"])
plt.ylabel("Average Quality Score")
plt.title("Smart Agriculture Quality Comparison")
plt.savefig("results/agriculture_quality_distribution.png")
plt.close()
