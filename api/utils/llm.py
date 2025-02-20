from ..config.settings import setting
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class calling_llm:
    def __init__(self):
        self.agent = setting
    
    def invoke(self, prompt: str) -> str:
        """
        Invoke the LLM with a prompt and return the response
        
        Args:
            prompt (str): The input prompt for the LLM
            
        Returns:
            str: The LLM's response
        """
        try:
            response = self.agent.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error invoking LLM: {str(e)}"