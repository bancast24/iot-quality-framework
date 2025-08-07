import sys
import subprocess

# Run Smart Agriculture Simulation
def run_agriculture_simulation():
    print("Running Smart Agriculture Simulation...")
    subprocess.run(["python", "Smart Agriculture Simulation/quality_agriculture.py"])

# Run Smart Industrial Simulation
def run_industrial_simulation():
    print("Running Smart Industrial Simulation...")
    subprocess.run(["python", "Smart Industrial Quality Evaluation/quality_industrail.py"])

# Entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify a simulation type: 'agriculture' or 'industrial'")
        sys.exit(1)

    simulation_type = sys.argv[1].lower()

    if simulation_type == "agriculture":
        run_agriculture_simulation()
    elif simulation_type == "industrial":
        run_industrial_simulation()
    else:
        print(f"Unknown simulation type: {simulation_type}")
        sys.exit(1)
