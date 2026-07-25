"""
Application configuration.

All application settings should be loaded from environment variables.
This keeps secrets and configuration outside the source code.
"""

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
MODEL_ID = os.getenv("MODEL_ID")