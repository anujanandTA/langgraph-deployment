import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables

LLM_API_KEY = os.environ["LLM_API_KEY"]
LLM_API_ENDPOINT = os.environ["LLM_API_ENDPOINT"]
LLM_MODEL = os.environ["LLM_MODEL"]
