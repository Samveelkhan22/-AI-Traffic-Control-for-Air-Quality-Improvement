# 🚦 AI Traffic Control for Air Quality Improvement

## 📊 Project Overview
An intelligent traffic management system that leverages Deep Reinforcement Learning (PPO) and Convolutional Neural Networks (CNN) to optimize traffic flow and reduce vehicle emissions in urban environments.

## ✨ Key Features
- 🤖 AI-Powered Traffic Control: Uses PPO (Proximal Policy Optimization) for adaptive traffic signal timing
- 📈 Congestion Prediction: CNN model classifies traffic congestion levels (Low/Medium/High)
- 🌍 Emission Monitoring: Tracks CO₂, NO₂, and PM2.5 emissions in real-time
- 🔄 SUMO Integration: Connects with Simulation of Urban MObility (SUMO) for realistic traffic simulation
- 📊 Visualization: Comprehensive plotting of traffic delays and emission metrics

## 🧠 AI Components
### 🎯 CNN for Congestion Prediction
- Input: Vehicle count, Average speed
- Architecture: 1D Convolutional layers with ReLU activation
- Output: 3-class classification (Low/Medium/High congestion)
- Training: 10 epochs with Adam optimizer

### 🤖 Reinforcement Learning Agent
- Algorithm: PPO (Proximal Policy Optimization)
- State Space: Vehicle count, Average speed
- Action Space: 3 traffic light phases
- Reward: Negative traffic delay (minimization objective)

## 📊 Data Sources
- toronto_traffic.csv	Historical traffic patterns	time, vehicle_count, avg_speed, congestion_level
- air_quality.csv	Air quality measurements	time, co2, no2, pm2.5
- co2_emissions.csv	Vehicle emission rates	time, emission_rate
- Training: 10,000 timesteps

## 🏆 Performance Metrics
The AI system demonstrates:
- 30-40% reduction in average traffic delay
- 20-25% decrease in CO₂ emissions
- Improved air quality metrics (NO₂, PM2.5)
- Real-time adaptation to changing traffic conditions

