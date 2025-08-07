import sys

# Function to run agriculture simulation
def run_agriculture_simulation():
    print("Running Smart Agriculture Simulation...")
    # Add agriculture simulation logic here

# Function to run industrial simulation
def run_industrial_simulation():
    print("Running Smart Industrial Simulation...")
    # Add industrial simulation logic here

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

*🐳 `docker-compose.yml` with simulation type specified:*

version: '3.8'

services:
  iot-quality-eval:
    build:.
    container_name: iot_quality_container
    working_dir: /app
    volumes:
      -.:/app
    command: python main.py agriculture
