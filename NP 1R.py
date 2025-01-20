import pyautogui
import time
import math

# Function to draw a small circle at the given position
def draw_circle(x, y, radius=10, steps=36):
    for angle in range(0, 360, int(360 / steps)):
        radian_angle = math.radians(angle)  # Convert angle to radians
        new_x = x + radius * math.cos(radian_angle)
        new_y = y + radius * math.sin(radian_angle)
        pyautogui.moveTo(new_x, new_y, duration=0.01)  # Smooth movement

# Main script
if __name__ == "__main__":
    # Ask user for the number of projects
    num_projects = int(input("Enter the number of projects: "))

    # Store run times for each project
    project_durations = []
    for i in range(1, num_projects + 1):
        print(f"Enter the duration for Project {i}:")
        project_hour = int(input(f"  Hour (for Project {i}): "))
        project_minute = int(input(f"  Minute (for Project {i}): "))
        project_durations.append(project_hour * 3600 + project_minute * 60)

    # Get screen width and height
    screen_width, screen_height = pyautogui.size()

    # Calculate positions for each project in the top half of the screen
    split_width = screen_width // num_projects
    y_position = int(screen_height * 0.25)  # Higher up, around 25% from the top

    positions = [
        (i * split_width + split_width // 2, y_position)
        for i in range(num_projects)
    ]

    # Run the script for each project
    for i in range(num_projects):
        print(f"Starting Project {i+1}")
        start_time = time.time()
        duration = project_durations[i]

        while time.time() - start_time < duration:
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

        # Close the project window using Alt+F4 after the project's duration
        pyautogui.hotkey("alt", "f4")
        print(f"Project {i+1} completed and window closed.")
