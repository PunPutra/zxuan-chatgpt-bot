from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("24269234", 0))
API_HASH = getenv("6b2aebf13c06fffc3a3500e8ad5b8f97", "")
BOT_TOKEN = getenv("5989086060:AAGj8ORiwshWJZLMpaHeP9HYsxTzqKf21YE", "")
OPENAI_API = getenv("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", "") # get api key : https://platform.openai.com/account/api-keys
