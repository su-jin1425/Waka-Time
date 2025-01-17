import pyautogui
import time
import math

def move_and_type_in_window(center_x, center_y, text, radius):
    # Perform actions in the specified window
    for angle in range(0, 180, 90):  # Quick cursor movement (only two positions per window)
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        pyautogui.moveTo(x, y, duration=0.1)  # Faster cursor movement
    
    pyautogui.leftClick()  # Focus the typing area
    pyautogui.write(text)  # Type the text
    pyautogui.press('enter')  # Press Enter
    pyautogui.hotkey('ctrl', 's')  # Save action

def main(total_duration, text="Hello, World!", radius=50):
    # Positions to focus each window sequentially
    window_positions = [
        (0.25, 0.25),  # Top-left
        (0.75, 0.25),  # Top-right
        (0.25, 0.75),  # Bottom-left
        (0.75, 0.75)   # Bottom-right
    ]
    
    # Get screen size to calculate relative positions
    screen_width, screen_height = pyautogui.size()

    start_time = time.time()
    while time.time() - start_time < total_duration:
        loop_start_time = time.time()
        for position in window_positions:
            # Focus the window using its center
            center_x = int(screen_width * position[0])
            center_y = int(screen_height * position[1])
            pyautogui.click(center_x, center_y)  # Activate window by clicking its center
            
            # Perform actions in the window
            move_and_type_in_window(center_x, center_y, text, radius)
        
        # Ensure the entire 4-window loop runs within 5 seconds
        elapsed_time = time.time() - loop_start_time
        if elapsed_time < 5:
            time.sleep(5 - elapsed_time)

if __name__ == "__main__":
    user_hours = int(input("Enter the duration in hours: "))
    user_minutes = int(input("Enter the duration in minutes: "))
    total_duration = (user_hours * 3600) + (user_minutes * 60)
    main(total_duration)
