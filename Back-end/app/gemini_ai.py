import google.generativeai as genai
import markdown

GOOGLE_API_KEY = 'AIzaSyDX2celKEp4nGzuUi0cdXrk2bMktGWY7Fs'  # Asegúrate de usar tu clave API real

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_prompt(prompt):
    response = model.generate_content(prompt)
    return response.text
