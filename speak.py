import os
import re
from gtts import gTTS
from playsound import playsound
import hashlib

def generate_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def speak(text):
    if not isinstance(text, str):
        text = str(text)
    try:
        # Extract the first line
        first_line = text.split('\n')[0]

        # Extract the first number from the line
        match = re.search(r'\d+', first_line)
        if match:
            number = match.group()

            # Generate hash for the number
            file_hash = generate_hash(number)

            # File path for the temporary voice
            file_path = f"{file_hash}.mp3"

            # Generate voice recording
            tts = gTTS(text=number, lang='en')
            tts.save(file_path)

            # Play the sound
            playsound(file_path)

            # Delete the temporary voice recording
            os.remove(file_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
