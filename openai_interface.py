import openai
import requests
from config import OPENAI_API_KEY, WOLFRAM_API_KEY
from screenshot import encode_image
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from collections import Counter
import os

os.environ['OPENAI_API_KEY'] = "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"

def get_content():
    try:
        # Initialize OpenAI API client
        openai.api_key = OPENAI_API_KEY

        # Path to image
        image_path = "screenshot.png"
        # Getting the base64 string
        base64_image = encode_image(image_path)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
            {   
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Answer the question correctly. The answer should be formatted in the same order as the answer choices in the image. For example, if the answer choices are '2. ___', '1. ___', '3. ___', the answer should be in the format '2. Answer for 2, 1. Answer for 1, 3. Answer for 3'."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
            "max_tokens": 4000
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        json_response = response.json()
        content = json_response['choices'][0]['message']['content']

        return content

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    content = get_content()
    print(content)