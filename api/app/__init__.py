
from dotenv import load_dotenv
import os
from fastapi import FastAPI  
from decouple import config

load_dotenv()
CONTACT_EMAIL = os.getenv("EMAIL") 
CONTACT_PASSWORD = os.getenv("PSWRD")
