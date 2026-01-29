from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 

# api_key = os.environ['API_KEY_OPENAI']
api_key = os.getenv("API_KEY_OPENAI")

llm = OpenAI(api_key=api_key)

pergunta = "me conte sobre a queda do bitcoin no dia de hoje"

resposta = llm.invoke(pergunta)

print(resposta)
print("test")