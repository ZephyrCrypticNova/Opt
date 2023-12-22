import base64
import pyautogui

def take_screenshot():
    try:
        # Define the region (left, top, width, height)
        region = (0, 450, 2600, 1050)  # Coordinates based on detected area
        
        # Take a screenshot of the defined region
        screenshot = pyautogui.screenshot(region=region)
        
        # Save the image
        screenshot.save("screenshot.png")

    except Exception as e:
        print(f"An error occurred while taking screenshot: {e}")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

if __name__ == "__main__":
    pass