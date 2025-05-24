from agents.query_agent import QueryAgent
from agents.summarization_agent import SummarizationAgent

class MultiAgentSystem:
    """
    Coordinates the workflow between multiple agents to process user queries
    about legal information.
    """
    
    def __init__(self, legal_documents):
        """
        Initialize the MultiAgentSystem with legal documents.
        
        Args:
            legal_documents (list): List of legal document dictionaries
        """
        self.legal_documents = legal_documents
        try:
            self.query_agent = QueryAgent(legal_documents)
            self.summarization_agent = SummarizationAgent()
        except Exception as e:
            print(f"Error initializing agents: {e}")
            raise
    
    def process_query(self, query, history=None):
        """
        Process a user query through the multi-agent system.
        
        Args:
            query (str): The user's query
            history (list, optional): List of previous messages
            
        Returns:
            str: The response to the user's query
        """
        try:
            relevant_information = self.query_agent.retrieve_information(query)
            
            if not relevant_information:
                return "I couldn't find specific information about that legal topic. Could you please provide more details or ask about a different legal matter?"
            
            summarized_response = self.summarization_agent.summarize(query, relevant_information)
            
            return summarized_response
        
        except Exception as e:
            print(f"Error in multi-agent system: {e}")
            return "I encountered an error while processing your query. Please try again."