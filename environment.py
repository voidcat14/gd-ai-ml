import gymnasium as gym
from gymnasium import spaces
import numpy as np
from mss import mss
import pydirectinput
import cv2
import json
import os

class GDVisualDataEnv(gym.Env):
    def __init__(self):
        super(GDVisualDataEnv, self).__init__()
        
        # Action: 0=Nothing, 1=Jump
        self.action_space = spaces.Discrete(2)
        
        # Observation: [PlayerX, PlayerY, NearestObstacleX]
        self.observation_space = spaces.Box(low=0, high=1920, shape=(3,), dtype=np.float32)
        
        self.sct = mss()
        # Adjust this to your game window
        self.monitor = {"top": 100, "left": 100, "width": 800, "height": 600}
        
        # LOAD COLORS FROM JSON
        self.load_colors()
        
        self.last_x = 0

    def load_colors(self):
        if os.path.exists("colors.json"):
            with open("colors.json", "r") as f:
                data = json.load(f)
                self.PLAYER_COLOR = np.array(data["player"]) if data["player"] else np.array([0, 255, 0])
                self.SPIKE_COLOR = np.array(data["spike"]) if data["spike"] else np.array([100, 100, 100])
        else:
            # Defaults if file doesn't exist
            self.PLAYER_COLOR = np.array([0, 255, 0])
            self.SPIKE_COLOR = np.array([100, 100, 100])

    def _extract_data(self):
        img = np.array(self.sct.grab(self.monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        
        # Find Player X
        mask = cv2.inRange(img, self.PLAYER_COLOR, self.PLAYER_COLOR)
        coords = np.column_stack(np.where(mask > 0))
        
        if len(coords) > 0:
            player_y, player_x = np.mean(coords, axis=0).astype(int)
        else:
            player_x, player_y = 0, 0
            
        # Find Nearest Obstacle
        obs_x = 800
        if player_x < 700:
            roi = img[:, player_x+10 : player_x+100]
            spike_mask = cv2.inRange(roi, self.SPIKE_COLOR, self.SPIKE_COLOR)
            spike_coords = np.column_stack(np.where(spike_mask > 0))
            if len(spike_coords) > 0:
                obs_x = player_x + spike_coords[0][1]
        
        return np.array([player_x, player_y, obs_x], dtype=np.float32)

    def step(self, action):
        if action == 1:
            pydirectinput.press('space')
        
        obs = self._extract_data()
        current_x = obs[0]
        
        if current_x <= self.last_x and current_x != 0:
            reward = -10
            done = True
        else:
            reward = current_x - self.last_x
            done = False
            
        self.last_x = current_x
        return obs, reward, done, False, {}

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.last_x = 0
        return self._extract_data(), {}
