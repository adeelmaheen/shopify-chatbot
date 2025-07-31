from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from pypdf import PdfReader
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

pdf_path = "./../cv.pdf"

# Load product knowledge from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

product_knowledge = extract_text_from_pdf(pdf_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    prompt = f"You are a customer support assistant. Use the following product knowledge to answer questions: {product_knowledge}\n\nUser: {user_message}"
    response = model.generate_content(prompt)
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)

