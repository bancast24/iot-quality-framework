import os

# Paths to each experiment
agriculture_path = "Smart Agriculture Smulation/quality_agriculture.py"
industrial_path = "Smart Industrial Quality Evaluation/quality_industrial.py"

# Run Smart Agriculture Simulation
print("Running Smart Agriculture Simulation...")
os.system(f"python \"{agriculture_path}\"")

# Run Smart Industrial Quality Evaluation
print("\nRunning Smart Industrial Quality Evaluation...")
os.system(f"python \"{industrial_path}\"")

print("\nAll experiments completed. Check the 'results' folders for outputs.")
