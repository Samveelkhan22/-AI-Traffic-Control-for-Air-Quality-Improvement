import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/simulation_results.csv")

plt.figure(figsize=(10,5))
plt.plot(df["step"], df["delay"], label="Traffic Delay")
plt.plot(df["step"], df["co2"], label="CO₂ Emissions", linestyle="dashed")
plt.xlabel("Time Steps")
plt.ylabel("Traffic Delay & Emissions")
plt.legend()
plt.title("Impact of AI Traffic Control on Air Quality")
plt.show()
