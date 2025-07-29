import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.GOOGLE_API_KEY = "AIzaSyCD_R-hjGCFRzHmxmz3robcnzQSpTJvIiY"
        self.SARVAM_API_KEY = "sk_jkx0d789_D56zB2BQZt10UoW5cTyz418Z"
        self.validate_keys()

    def validate_keys(self):
        if not self.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment. Please set it in your .env file.")
        if not self.SARVAM_API_KEY:
            raise ValueError("SARVAM_API_KEY not found in environment. Please set it in your .env file.")
