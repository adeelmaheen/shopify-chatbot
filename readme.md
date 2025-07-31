🛍️ Shopify Chatbot with Google Gemini API
📌 Overview
This project integrates a custom AI-powered chatbot into a Shopify store using the Google Gemini API. The chatbot is designed to assist customers by providing real-time responses based on detailed product information extracted from a PDF document.

🔧 Features
AI-Powered Assistance: Utilizes Google Gemini API for intelligent responses.

Product Knowledge Integration: Extracts and incorporates product details from a PDF.

Shopify Integration: Seamlessly integrates with Shopify stores.

Customizable Responses: Tailor the chatbot's behavior and knowledge base.

🛠️ Technologies Used
Backend: Python with Flask

AI: Google Gemini API

PDF Parsing: PyPDF2

Frontend: JavaScript for chatbot widget

Shopify: Liquid templating for integration

📁 Project Structure
bash
Copy
/shopify-gemini-chatbot
│
├── /public
│   └── chatbot-widget.js       # Frontend widget script
│
├── /server
│   ├── app.py                  # Flask backend
│   └── requirements.txt        # Python dependencies
│
└── /shopify
    └── gemini_integration.liquid  # Shopify Liquid template
🚀 Installation & Setup
1. Clone the Repository
bash
Copy
git clone https://github.com/yourusername/shopify-gemini-chatbot.git
cd shopify-gemini-chatbot
2. Set Up Backend
Navigate to the /server directory.

Create a virtual environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy
pip install -r requirements.txt
Obtain your Google Gemini API key and set it in the app.py file:

python
Copy
client = genai.Client(api_key='YOUR_GEMINI_API_KEY')
Run the Flask application:

bash
Copy
python app.py
3. Set Up Frontend
Upload the chatbot-widget.js file to your Shopify store's assets.

Create a new Liquid template (gemini_integration.liquid) and include the following code:

liquid
Copy
<script src="{{ 'chatbot-widget.js' | asset_url }}"></script>
Include this template in your Shopify theme's layout to load the chatbot widget on desired pages.

4. Extract Product Knowledge from PDF
Place your product PDF in the /server directory.

The app.py script automatically extracts text from the PDF and integrates it into the chatbot's knowledge base.

🧪 Testing Locally
Ensure the Flask server is running:

bash
Copy
python app.py
Open your Shopify store's frontend in a browser.

Interact with the chatbot widget to test its functionality.

📄 License
This project is licensed under the MIT License.