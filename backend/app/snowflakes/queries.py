import app.snowflakes.database as db

# SQL queries
account_query = "SELECT * FROM salesforce_db.raw_data.account"
activities_features_query = "SELECT * FROM salesforce_db.feature_data.activities_features"
companies_features_query = "SELECT * FROM salesforce_db.feature_data.companies_features"
features_query = "SELECT * FROM salesforce_db.feature_data.features"

def get_account_data():
    return db.get_table(account_query)

def get_activities_features():
    return db.get_table(activities_features_query)

def get_companies_features():
    return db.get_table(companies_features_query)

def get_features_data():
    return db.get_table(features_query)
