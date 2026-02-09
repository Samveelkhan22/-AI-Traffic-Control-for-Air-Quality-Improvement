import pandas as pd

def load_traffic_data():
    df = pd.read_csv("datasets/toronto_traffic.csv")
    df = df[["time", "vehicle_count", "avg_speed", "congestion_level"]]
    return df

def load_air_quality_data():
    df = pd.read_csv("datasets/air_quality.csv")
    return df[["time", "co2", "no2", "pm2.5"]]

def load_co2_emissions_data():
    df = pd.read_csv("datasets/co2_emissions.csv")
    return df[["time", "emission_rate"]]

traffic_data = load_traffic_data()
air_quality_data = load_air_quality_data()
co2_data = load_co2_emissions_data()
