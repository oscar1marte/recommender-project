import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import app.snowflakes.queries as queries

numerical_cols = ['GROWTH_RATE__C', 'TOTAL_FUNDING_TO_DATE__C', 'NUMBEROFEMPLOYEES']
filter_list = [
    ['RATING_HOT', 'RATING_WARM', 'RATING_COLD'],
    ['HQ_LOCATION__C_NORTHEAST', 'HQ_LOCATION__C_WEST', 'HQ_LOCATION__C_SOUTHWEST', 'HQ_LOCATION__C_SOUTHEAST', 'HQ_LOCATION__C_MIDWEST'],
    ['INDUSTRY_TECHNOLOGY_AND_COMMUNICATIONS', 'INDUSTRY_FINANCE_AND_INSURANCE', 'INDUSTRY_CONSUMER_AND_SERVICES', 'INDUSTRY_INDUSTRIAL_AND_OTHER'],
    ['TOTAL_FUNDING_TO_DATE__C'],
    ['TYPE_ACC_ESTABLISHED', 'TYPE_ACC_GROWTH_STAGE', 'TYPE_ACC_STARTUP'],
    ['RANGE_ANNUALREVENUE_HIGH', 'RANGE_ANNUALREVENUE_LOW', 'RANGE_ANNUALREVENUE_LOWER_MIDDLE', 'RANGE_ANNUALREVENUE_UPPER_MIDDLE'],
    ['OWNERSHIP_PRIVATE', 'OWNERSHIP_PUBLIC', 'OWNERSHIP_SUBSIDIARY'],
    ['OWNER_INTENT_TO_SELL__C']
]

def get_features_and_scaler():
    features_acc = queries.get_features_data()
    scaler = StandardScaler()
    features_acc[numerical_cols] = scaler.fit_transform(features_acc[numerical_cols])
    return features_acc, scaler

def create_user_profile(user_values, features_acc, numerical_cols, scaler):
    profile = pd.DataFrame(np.zeros((1, len(features_acc.columns))), columns=features_acc.columns)
    for key, value in user_values.items():
        if key in profile.columns:
            profile.at[0, key] = value
        else:
            print(f"Warning: {key} is not a valid column name.")
    profile[numerical_cols] = scaler.transform(profile[numerical_cols])
    profile_features = profile[user_values.keys()]
    return profile_features

def transform_api_response(api_response):
    columns = api_response.keys()
    values_dict = {column: api_response[column] for column in columns}
    
    ids = values_dict['ID'].keys()
    
    transformed_data = []
    for id in ids:
        entry = {column: values_dict[column][id] for column in columns}
        transformed_data.append(entry)
    
    return transformed_data

def transform_dict_to_input(user_values, industry_mapping, location_mapping):
    user_values_input = {}
    if 'RATING' in user_values.keys():
        user_values_input[f"RATING_{user_values['RATING']}"] = 1
    if 'HQ_LOCATION__C' in user_values.keys():
        user_values_input[location_mapping[user_values['HQ_LOCATION__C']]] = 1
    if 'INDUSTRY' in user_values.keys():
        user_values_input[industry_mapping[user_values['INDUSTRY']]] = 1
    if 'OWNERSHIP' in user_values.keys():
        user_values_input[f"OWNERSHIP_{user_values['OWNERSHIP']}"] = 1
    if 'TYPE_ACC' in user_values.keys():
        user_values_input[f"TYPE_ACC_{user_values['TYPE_ACC']}"] = 1
    if 'OWNER_INTENT_TO_SELL__C' in user_values.keys():
        user_values_input["OWNER_INTENT_TO_SELL__C"] = 1
    
    return user_values_input

def generate_default_user_profile(companies_features):
    keys = []
    values = []
    for filters in filter_list:
        feature_name = None
        feature_coeff = 0
        for filter in filters:
            filter_df = companies_features[companies_features.FEATURE == filter]
            if filter_df.COEFFICIENT.values[0] >= feature_coeff:
                feature_name = filter_df.FEATURE.values[0]
                feature_coeff = filter_df.COEFFICIENT.values[0]
        keys.append(feature_name)
        values.append(feature_coeff)
    
    default_df = pd.DataFrame(data={"FEATURE": keys, "VALUES": values}).sort_values(by="VALUES", ascending=False).head(5)

    return  dict(zip(default_df.FEATURE.to_list(), [1]*5))
    