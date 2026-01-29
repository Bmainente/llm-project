from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 

llm = OpenAI(API_KEY_OPENAI)

pergunta = "me conte sobre a queda do bitcoin no dia de hoje"

resposta = llm.invoke(pergunta)

print(resposta)
print("test")