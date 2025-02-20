# This can be empty or you can add:
from .llm import calling_llm

llm_instance = calling_llm()

__all__ = ['llm_instance']