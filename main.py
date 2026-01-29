from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 

llm = OpenAI()

pergunta = "me fale sobre os hipopotamos"

resposta = llm.invoke(pergunta)

print(resposta)
print("test")