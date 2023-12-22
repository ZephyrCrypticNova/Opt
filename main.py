# main.py
import schedule
import time
from screenshot import take_screenshot
from openai_interface import get_content
from speak import speak
#change
def main():
    try:
        # Take a screenshot of the current screen
        take_screenshot()

        answer = get_content()

        speak(answer)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Schedule the main function to run every 12 seconds
    schedule.every(10).seconds.do(main)

    # Delay the start of the schedule by 10 minutes
    #time.sleep(500)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)