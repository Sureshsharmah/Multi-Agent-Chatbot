from flask import Flask, render_template, request, jsonify
from agents.multi_agent_system import MultiAgentSystem
from data.legal_documents import LEGAL_DOCUMENTS
import config
import re

app = Flask(__name__)
app.config.from_object(config)

try:
    multi_agent_system = MultiAgentSystem(LEGAL_DOCUMENTS)
    print("Multi-agent system initialized successfully!")
except Exception as e:
    print(f"Failed to initialize multi-agent system: {e}")
    multi_agent_system = None

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Process a chat message and return a response."""
    try:
        if not multi_agent_system:
            return jsonify({'error': 'System not properly initialized'}), 500
            
        data = request.json
        message = data.get('message', '')
        history = data.get('history', [])
        
        if not message.strip():
            return jsonify({'error': 'Empty message'}), 400
        
        response = multi_agent_system.process_query(message, history)
        
        return jsonify({'response': response})
    
    except Exception as e:
        print(f"Error in chat API: {e}")
        return jsonify({'error': 'Failed to process your request'}), 500

if __name__ == '__main__':
    print("Starting Legal Assistant Chatbot...")
    print("Make sure your .env file contains:")
    print("- AZURE_OPENAI_API_KEY")
    print("- AZURE_OPENAI_ENDPOINT") 
    print("- AZURE_OPENAI_DEPLOYMENT")
    print("- AZURE_RESOURCE_NAME")
    app.run(debug=config.DEBUG)