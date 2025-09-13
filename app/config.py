from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

embed1 = GoogleGenerativeAIEmbeddings(
    model='models/embedding-001',
    google_api_key=GOOGLE_API_KEY
)

embed = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=GOOGLE_API_KEY)
