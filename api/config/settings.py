from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class llmAgent:
    ChatGroq(api_key=GROQ_API_KEY, model="qwen-2.5-32b", max_tokens=None)

setting = llmAgent()