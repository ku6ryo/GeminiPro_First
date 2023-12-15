import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

genai.configure(api_key=os.getenv("GENAI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

history = []

while True:
    data = input("You: ")
    history.append({
        'parts': [data],
        'role': 'user'
    })
    response = model.generate_content(history)
    print("Model: ", response.text)
    history.append({
        'parts': [response.text],
        'role': 'model'
    })  
