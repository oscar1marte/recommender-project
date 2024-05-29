import os
from dotenv import load_dotenv

# Construct the path to the .env file
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')

# Load the .env file
load_dotenv(env_path)

class Settings:
    def __init__(self):
        self.account = os.getenv('SNOWFLAKE_ACCOUNT')
        self.user = os.getenv('SNOWFLAKE_USER')
        self.password = os.getenv('SNOWFLAKE_PASSWORD')
        self.database = os.getenv('SNOWFLAKE_DATABASE')
        self.schema = os.getenv('SNOWFLAKE_SCHEMA')
        self.warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')

settings = Settings()
