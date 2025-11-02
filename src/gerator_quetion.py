import groq
import dotenv
import os

dotenv.load_dotenv(".env")

groq_key = os.getenv("groq_api")


client = groq.Groq(api_key=groq_key)

system_prompt = """

"""
