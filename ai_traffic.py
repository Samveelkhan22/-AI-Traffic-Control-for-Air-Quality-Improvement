import traci
import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from stable_baselines3 import PPO
from load_data import load_traffic_data

# 🔹 Load dataset
traffic_data = load_traffic_data()

# 🔹 Train CNN for Congestion Prediction
cnn_model = Sequential([
    tf.keras.layers.Conv1D(64, 2, activation="relu", input_shape=(2, 1)),  # Fixed input shape
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")  # 3 classes: Low, Medium, High congestion
])
cnn_model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Reshape inputs correctly
X_train = traffic_data[["vehicle_count", "avg_speed"]].values.reshape(-1, 2, 1)  # Fixed input shape
y_train = traffic_data["congestion_level"].values
cnn_model.fit(X_train, y_train, epochs=10, batch_size=16)
cnn_model.save("models/cnn_traffic")

# 🔹 AI Traffic Signal Control (Reinforcement Learning with PPO)
class TrafficEnv(gym.Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()
        self.action_space = gym.spaces.Discrete(3)  # 3 traffic light phases
        self.observation_space = gym.spaces.Box(low=0, high=100, shape=(2,), dtype=np.float32)  # Fixed observation shape

    def get_real_time_state(self):
        """Retrieve real-time traffic data from SUMO."""
        vehicle_count = traci.edge.getLastStepVehicleNumber("AtoB")
        avg_speed = traci.edge.getLastStepMeanSpeed("AtoB")
        return np.array([vehicle_count, avg_speed], dtype=np.float32)  # Fixed shape

    def step(self, action):
        traci.simulationStep()
        obs = self.get_real_time_state()
        
        congestion = np.argmax(cnn_model.predict(obs.reshape(1, 2, 1)))  # Fixed shape

        # AI-based Traffic Signal Adjustment
        if congestion == 2:
            traci.trafficlight.setPhase("A", 2)
        elif congestion == 1:
            traci.trafficlight.setPhase("A", 1)
        else:
            traci.trafficlight.setPhase("A", 0)

        delay = traci.edge.getWaitingTime("AtoB")
        reward = -delay  # Minimize delay
        done = False  # Traffic simulation doesn't "end" like a game
        info = {}  # Empty dictionary for compatibility

        return obs, reward, done, info  # Fixed return format

    def reset(self):
        traci.start(["sumo", "-c", "simple.sumocfg"])
        return self.get_real_time_state()

# 🔹 Train PPO Model
env = TrafficEnv()
ppo_model = PPO("MlpPolicy", env, verbose=1)
ppo_model.learn(total_timesteps=10000)
ppo_model.save("models/ppo_traffic")
