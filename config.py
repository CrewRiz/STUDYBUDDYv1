import os
import logging

# Configuration
TUTOR_ASSISTANT_ID = 'asst_30iv40wmV0pKqjE3XluIuR9l'
NOTES_ASSISTANT_ID = 'asst_8m20MnOFZZdSAcl07IfLgTgg'

# Logging setup
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# API Key
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise EnvironmentError("OPENAI_API_KEY is not set in the environment variables")