import snowflake.connector
import pandas as pd
from app.core.config import settings

# Global variable to hold the connection context
ctx = None

def create_connection():
    global ctx
    ctx = snowflake.connector.connect(
        user=settings.user,
        password=settings.password,
        account=settings.account,
        database=settings.database,
        schema=settings.schema,
        warehouse=settings.warehouse
    )

def get_table(query):
    global ctx
    if ctx is None:
        raise ValueError("Database connection is not established. Call 'create_connection' first.")
    
    cs = ctx.cursor()
    try:
        cs.execute(query)
        df = cs.fetch_pandas_all()
    finally:
        cs.close()
    return df

def close_connection():
    global ctx
    if ctx is not None:
        ctx.close()
        ctx = None

if __name__ == "__main__":
    create_connection()
    try:
        query = "SELECT * FROM salesforce_db.raw_data.account Limit 1"
        df = get_table(query)
        print(df)
    finally:
        close_connection()
