import os

from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")


if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY não configurada.")

if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY não configurada.")