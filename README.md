# Multi-Agent-Chatbot

Multi-Agent-Chatbot
Multi-Agent Legal Assistant Chatbot An AI-powered legal assistant that fetches information from trusted legal documents, summarizes complex concepts, and provides clear answers using a multi-agent architecture.

🚀 Key Features Query Agent: Retrieves precise legal sections from documents Summarization Agent: Converts complex legal jargon into plain language Multi-Agent Collaboration: Agents work together to provide comprehensive answers Production-Ready: Flask backend with clean API design 📦 Installation Clone the repository git clone https://github.com/Sureshsharmah/Multi-Agent-Chatbot.git cd Multi-Agent-Chatbot Set up virtual environment

bash python -m venv venv

For Linux/Mac: source venv/bin/activate

For Windows: venv\Scripts\activate Install dependencies

bash pip install -r requirements.txt Configure environment variables Create .env file in the root directory with:

AZURE_OPENAI_API_KEY=your_key_here AZURE_OPENAI_ENDPOINT=your_endpoint AZURE_OPENAI_DEPLOYMENT=deployment_name AZURE_RESOURCE_NAME=resource_name 🖥️ Running the Application Development mode:

bash python app.py Production mode (with Gunicorn):

bash gunicorn app:app --bind 0.0.0.0:5000 --timeout 120 Access the app at: http://localhost:5000

🌐 API Endpoints Endpoint Method Description / GET Web interface /api/chat POST Process legal queries (payload: {"message": "your query"}) 📚 Data Sources Guide to Litigation in India

Legal Compliance & Corporate Laws by ICAI

🛠️ Challenges & Solutions Challenge Solution Legal text complexity Hybrid extractive-abstractive summarization Response accuracy Document verification layer Performance Cached frequent queries 📈 Future Improvements Add citation to legal provisions

Implement follow-up question handling

Expand document database

Here are some questions from the documents Litigation Questions: 

### Litigation Questions:

1. "What are the steps involved in filing a lawsuit in India?"
2. "How does the court hierarchy work in India?"
3. "What is the role of an advocate in Indian legal proceedings?"
4. "What happens after a lawsuit is filed in an Indian court?"
5. "What is the process for serving summons in India?"


### Corporate Law Questions:

1. "How is a company formed in India?"
2. "What are the requirements for corporate governance in India?"
3. "What are the key taxation laws applicable to companies in India?"
4. "What is the process for obtaining a Director Identification Number in India?"
5. "What are the mandatory committees required for public companies in India?"


### General Legal Questions:

1. "What is the difference between civil and criminal cases in India?"
2. "What are the legal requirements for board meetings in Indian companies?"
3. "How does Corporate Social Responsibility work in India?"
4. "What are the different types of advocates in the Indian legal system?"
5. "What is the role of the Registrar of Companies in India?"
