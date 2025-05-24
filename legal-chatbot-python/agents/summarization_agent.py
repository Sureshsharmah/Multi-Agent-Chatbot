import openai
from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_API_VERSION
)

class SummarizationAgent:
    """
    Agent responsible for summarizing and simplifying complex legal information.
    """
    
    def __init__(self):
        """Initialize the SummarizationAgent."""
        openai.api_type = "azure"
        openai.api_key = AZURE_OPENAI_API_KEY
        openai.api_base = AZURE_OPENAI_ENDPOINT
        openai.api_version = AZURE_API_VERSION
        
        print("Summarization Agent initialized successfully!")
    
    def summarize(self, query, sections):
        """
        Summarize and simplify the legal information from the provided sections.
        
        Args:
            query (str): The user's query
            sections (list): List of relevant document sections
            
        Returns:
            str: Simplified summary of the legal information
        """
        try:
            combined_content = "\n\n".join([
                f"From {section.get('document_title', 'Unknown Document')} - {section['title']}:\n{section['content']}"
                for section in sections
            ])
            
            if len(combined_content) > 8000:
                combined_content = combined_content[:8000] + "..."
            
            system_message = """You are a legal assistant specialized in Indian law. Your task is to:
                                1. Simplify complex legal concepts into plain, easy-to-understand language
                                2. Provide accurate information based on the legal documents
                                3. Structure your response in a clear, concise manner
                                4. If appropriate, use numbered steps for procedures
                                5. Avoid legal jargon when possible, but explain necessary legal terms
                                6. End with a follow-up question if appropriate"""
            
            user_message = f"""User query: "{query}"

Relevant legal information:
{combined_content}

Please provide a clear, simplified explanation that answers the user's query based on this information."""
            
            response = openai.ChatCompletion.create(
                engine=AZURE_OPENAI_DEPLOYMENT,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=800
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            print(f"Error in summarization agent: {e}")
            return f"I found information about your query regarding '{query}', but I'm having trouble processing it right now. Please try rephrasing your question or ask about a specific aspect of the topic."