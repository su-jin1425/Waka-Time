import pyautogui
import time
import math

def move_and_type(duration_hours, duration_minutes, interval=5, text="Hello, World!", radius=50):
    total_duration = (duration_hours * 3600) + (duration_minutes * 60)  # Convert hours and minutes to seconds
    start_time = time.time()
    
    center_x, center_y = pyautogui.position()  # Start from the current position
    
    while time.time() - start_time < total_duration:
        # Move the cursor in a small circular pattern
        for angle in range(0, 360, 10):  # Angle changes in increments of 10 degrees
            # Calculate the new position for the cursor based on sine and cosine functions
            x = center_x + radius * math.cos(math.radians(angle))
            y = center_y + radius * math.sin(math.radians(angle))
            pyautogui.moveTo(x, y)
        
        pyautogui.leftClick()  # Perform left-click to focus the typing area
        pyautogui.write(text)  # Type the text
        pyautogui.press('enter')  # Press 'Enter' after typing to move to the next line
        pyautogui.hotkey('ctrl', 's')  # Perform Ctrl + S (Save)
        
        time.sleep(interval)  # Wait for the interval before repeating the loop

# Example usage:
user_hours = int(input("Enter the duration in hours: "))
user_minutes = int(input("Enter the duration in minutes: "))
move_and_type(user_hours, user_minutes)
