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

Here are some questions from the documents Litigation Questions: "What are the steps involved in filing a lawsuit in India?" "How does the court hierarchy work in India?" "What is the role of an advocate in Indian legal proceedings?" "What happens after a lawsuit is filed in an Indian court?" "What is the process for serving summons in India?" Corporate Law Questions: "How is a company formed in India?" "What are the requirements for corporate governance in India?" "What are the key taxation laws applicable to companies in India?" "What is the process for obtaining a Director Identification Number in India?" "What are the mandatory committees required for public companies in India?" General Legal Questions: "What is the difference between civil and criminal cases in India?" "What are the legal requirements for board meetings in Indian companies?" "How does Corporate Social Responsibility work in India?" "What are the different types of advocates in the Indian legal system?" "What is the role of the Registrar of Companies in India?" About No description, website, or topics provided. Resources Readme Activity Stars 0 stars Watchers 0 watching Forks 0 forks Releases No releases published Create a new release Packages No packages published Publish your first package Languages Python 68.9%

JavaScript 12.9%

CSS 12.1%

HTML 6.0%

Procfile 0.1% Suggested workflows Based on your tech stack Python Package using Anaconda logo Python Package using Anaconda Create and test a Python package on multiple Python versions using Anaconda for package management. Python application logo Python application Create and test a Python application. Pylint logo Pylint Lint a Python application with pylint. More workflows Footer

About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Footer
© 2025
