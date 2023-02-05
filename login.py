import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

bot_token = os.getenv("bot_token")
bot_chatID = os.getenv("bot_chatID")

