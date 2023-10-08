
from dotenv import load_dotenv
import os
from fastapi import FastAPI  
from decouple import config

load_dotenv()
MAIL_USERNAME = os.getenv("EMAIL") 
MAIL_PASSWORD = os.getenv("PSWRD")
