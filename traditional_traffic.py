# import traci

# def run_fixed_signal():
#     traci.start(["sumo", "-c", "simple.sumocfg"])
    
#     for step in range(1000):
#         traci.simulationStep()

#         if step % 30 == 0:
#             traci.trafficlight.setPhase("A", 0)
#         elif step % 60 == 0:
#             traci.trafficlight.setPhase("A", 1)
#         elif step % 90 == 0:
#             traci.trafficlight.setPhase("A", 2)
    
#     traci.close()

# run_fixed_signal()

import traci

SUMO_BINARY = "C:/Program Files (x86)/Eclipse/Sumo/bin/sumo.exe"
CONFIG_FILE = "D:/Users/J.I Traders/Desktop/Projects/Traffic Managment/Scripts/simple.sumocfg"

try:
    traci.start([SUMO_BINARY, "-c", CONFIG_FILE, "--start", "--log", "sumo_debug.log", "--verbose"])
    print("SUMO started successfully!")
except Exception as e:
    print(f"Error starting SUMO: {e}")

# Keep SUMO running for debugging
import time
time.sleep(5)

# Close SUMO safely
traci.close()
