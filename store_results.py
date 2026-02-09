import pandas as pd
import traci

results = []

for step in range(1000):
    traci.simulationStep()

    delay = traci.edge.getWaitingTime("AtoB")
    co2 = traci.vehicle.getCO2Emission("car1")

    results.append([step, delay, co2])

traci.close()

df = pd.DataFrame(results, columns=["step", "delay", "co2"])
df.to_csv("datasets/simulation_results.csv", index=False)
