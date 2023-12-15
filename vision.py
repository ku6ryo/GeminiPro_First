from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()


genai.configure(api_key=os.getenv("GENAI_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")
img = Image.open("images/hotel.jpg")
response = model.generate_content([
    "この画像の内容について説明してください。",
    img
], stream=True)
response.resolve()

print(response.text)
