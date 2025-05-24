import openai
import os
from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_API_VERSION
)

class QueryAgent:
    """
    Agent responsible for retrieving relevant information from legal documents
    based on user queries.
    """
    
    def __init__(self, legal_documents):
        """
        Initialize the QueryAgent with legal documents.
        
        Args:
            legal_documents (list): List of legal document dictionaries
        """
        self.legal_documents = legal_documents
        
        openai.api_type = "azure"
        openai.api_key = AZURE_OPENAI_API_KEY
        openai.api_base = AZURE_OPENAI_ENDPOINT
        openai.api_version = AZURE_API_VERSION
        
        print("Query Agent initialized successfully!")
    
    def retrieve_information(self, query):
        """
        Retrieve relevant information from legal documents based on the user query.
        
        Args:
            query (str): The user's query
            
        Returns:
            list: List of relevant document sections
        """
        try:
            relevant_documents = self._identify_relevant_documents(query)
            
            if not relevant_documents:
                return []
            
            relevant_sections = self._extract_relevant_sections(query, relevant_documents)
            
            return relevant_sections
        
        except Exception as e:
            print(f"Error in query agent: {e}")
            raise Exception(f"Failed to retrieve information: {e}")
    
    def _identify_relevant_documents(self, query):
        """
        Identify which documents are most relevant to the user query.
        
        Args:
            query (str): The user's query
            
        Returns:
            list: List of relevant document dictionaries
        """
        try:
            prompt = f"""I have the following legal documents:
{chr(10).join([f"- {doc['title']}: {doc['description']}" for doc in self.legal_documents])}

Based on the user query: "{query}"

Which of these documents would be most relevant? Return only the titles of the relevant documents, separated by commas."""
            
            response = openai.ChatCompletion.create(
                engine=AZURE_OPENAI_DEPLOYMENT,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.3
            )
            
            relevant_titles = response.choices[0].message.content.strip().split(',')
            relevant_titles = [title.strip() for title in relevant_titles]
            
            return [
                doc for doc in self.legal_documents
                if any(title.lower() in doc['title'].lower() for title in relevant_titles)
            ]
        except Exception as e:
            print(f"Error identifying relevant documents: {e}")
            return self.legal_documents
    
    def _extract_relevant_sections(self, query, documents):
        """
        Extract relevant sections from the identified documents.
        
        Args:
            query (str): The user's query
            documents (list): List of relevant document dictionaries
            
        Returns:
            list: List of relevant section dictionaries
        """
        relevant_sections = []
        
        for document in documents:
            try:
                sections_text = "\n\n".join([
                    f"Section {section['id']}: {section['title']}\n{section['content'][:200]}..."
                    for section in document['sections']
                ])
                
                prompt = f"""Document: {document['title']}

Sections:
{sections_text}

User query: "{query}"

Identify the section IDs that are most relevant to answering this query. Return only the section IDs, separated by commas."""
                
                response = openai.ChatCompletion.create(
                    engine=AZURE_OPENAI_DEPLOYMENT,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=50,
                    temperature=0.3
                )
                
                relevant_section_ids = response.choices[0].message.content.strip().split(',')
                relevant_section_ids = [section_id.strip() for section_id in relevant_section_ids]
                
                for section in document['sections']:
                    if section['id'] in relevant_section_ids:
                        section_with_doc = section.copy()
                        section_with_doc['document_title'] = document['title']
                        relevant_sections.append(section_with_doc)
            
            except Exception as e:
                print(f"Error extracting sections from {document['title']}: {e}")
                for section in document['sections']:
                    section_with_doc = section.copy()
                    section_with_doc['document_title'] = document['title']
                    relevant_sections.append(section_with_doc)
        
        return relevant_sections