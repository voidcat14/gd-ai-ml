import time
import cv2
import numpy as np
from environment import GDEnv

def test_env():
    env = GDEnv()
    print("Starting test in 3 seconds... Switch to Geometry Dash!")
    time.sleep(3)
    
    try:
        while True:
            obs, _ = env.reset()
            # Convert the observation for OpenCV display (remove channel dim)
            display_img = obs[:, :, 0]
            
            # Show the AI's vision
            cv2.imshow('AI Vision', display_img)
            
            # Simple test: Jump every 2 seconds
            # In a real AI, the 'action' comes from the model
            action = 1 if (int(time.time()) % 2 == 0) else 0
            
            obs, reward, done, _, _ = env.step(action)
            
            if action == 1:
                print("JUMP!")
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    test_env()
