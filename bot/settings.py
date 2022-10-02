import os
from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN')

WEBHOOK = {
   'URL': os.getenv('WEBHOOK_URL'),
   'PATH': os.getenv('WEBHOOK_PATH'),
}

SERVER = {
   'HOST': os.getenv('SERVER_HOST'),
   'PORT': os.getenv('SERVER_PORT') if os.getenv('SERVER_PORT') else os.getenv('PORT'),  # определение порта для Heroku
}