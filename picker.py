import pyautogui
import numpy as np
import json
import time

def pick_colors():
    print("--- GD AI Color Picker ---")
    print("1. Open Geometry Dash and enter a level.")
    print("2. Hover your mouse over your PLAYER icon and press 'S' to save.")
    print("3. Hover your mouse over a SPIKE and press 'P' to save.")
    print("4. Press 'Q' to quit.")
    
    colors = {"player": None, "spike": None}
    
    try:
        while True:
            # Check for keyboard input (simple way)
            import keyboard # Need to pip install keyboard
            
            if keyboard.is_pressed('s'):
                x, y = pyautogui.position()
                color = pyautogui.pixel(x, y)
                colors["player"] = color
                print(f"Saved Player Color: {color}")
                time.sleep(0.5) # Prevent double-save
                
            if keyboard.is_pressed('p'):
                x, y = pyautogui.position()
                color = pyautogui.pixel(x, y)
                colors["spike"] = color
                print(f"Saved Spike Color: {color}")
                time.sleep(0.5)
                
            if keyboard.is_pressed('q'):
                break
    except KeyboardInterrupt:
        pass
    
    with open("colors.json", "w") as f:
        json.dump(colors, f)
    print("Colors saved to colors.json! You can now start the AI.")

if __name__ == "__main__":
    pick_colors()
