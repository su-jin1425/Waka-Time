import pyautogui
import time
import math

# Function to draw a small circle at the given position
def draw_circle(x, y, radius=10, steps=36):
    for angle in range(0, 360, int(360 / steps)):
        radian_angle = math.radians(angle)  # Convert angle to radians
        new_x = x + radius * math.cos(radian_angle)
        new_y = y + radius * math.sin(radian_angle)
        pyautogui.moveTo(new_x, new_y, duration=0.01)  # Smooth movement for drawing the circle

# Main script
if __name__ == "__main__":
    # Ask user for total duration
    hours = int(input("Enter the total duration in hours: "))
    minutes = int(input("Enter the total duration in minutes: "))

    # Ask for number of circles and their positions
    num_circles = int(input("Enter the number of circles: "))
    positions = []
    for i in range(num_circles):
        x = int(input(f"Enter the x-coordinate for circle {i + 1}: "))
        y = int(input(f"Enter the y-coordinate for circle {i + 1}: "))
        positions.append((x, y))

    # Calculate the total duration in seconds
    total_duration = hours * 3600 + minutes * 60
    start_time = time.time()

    # Main loop
    while time.time() - start_time < total_duration:
        loop_start_time = time.time()

        for x, y in positions:
            # Move to the position and left-click to focus
            pyautogui.moveTo(x, y, duration=0.2)  # Smooth movement
            pyautogui.click()  # Left-click to focus

            # Draw a small circle
            draw_circle(x, y)

            # Left-click again, type "hello world", and press Enter
            pyautogui.click()
            pyautogui.typewrite("hello world")
            pyautogui.press("enter")

            # Save (Ctrl+S)
            pyautogui.hotkey("ctrl", "s")

        # Calculate the total elapsed time for the loop
        total_elapsed = time.time() - loop_start_time

        # Ensure the entire loop (all circles) finishes within 5 seconds
        if total_elapsed < 5:
            time.sleep(5 - total_elapsed)
