import gymnasium as gym
from stable_baselines3 import PPO
from environment import GDDataEnv
import os

def train_ai():
    # Create the custom Data-Driven Environment
    env = GDDataEnv()
    
    # Check if we successfully attached to GD
    if env.pm is None:
        print("Error: Geometry Dash is not running. Please open the game first!")
        return

    # Initialize the PPO Model (Proximal Policy Optimization)
    # MlpPolicy = Multi-layer Perceptron (best for numeric data vectors)
    model = PPO("MlpPolicy", env, verbose=1, learning_rate=0.0003, tensorboard_log="./gd_tensorboard/")

    print("AI is now training... Switch to Geometry Dash and let it play!")
    
    try:
        # Train for 100,000 steps
        # The AI will learn: "When X is at this point and Y is this, Jump!"
        model.learn(total_timesteps=100000)
        
        # Save the trained brain
        model.save("gd_ai_model")
        print("Training complete! Model saved as gd_ai_model.zip")
        
    except KeyboardInterrupt:
        print("Training interrupted by user. Saving current progress...")
        model.save("gd_ai_model_interrupted")

if __name__ == "__main__":
    train_ai()
