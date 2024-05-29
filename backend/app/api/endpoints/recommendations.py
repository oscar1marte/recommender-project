from fastapi import APIRouter, HTTPException
from app.models.user_profile import UserProfile
import app.services.data_processing as dp
import app.services.recommendation as rec
import app.snowflakes.queries as queries
from app.mappings.mapping import industry_mapping, location_mapping

router = APIRouter()

@router.post("/recommendations/")
def get_recommendations(user_profile: UserProfile):
    user_values = user_profile.dict()
    user_values = dp.transform_dict_to_input(user_values, industry_mapping, location_mapping)
    features_acc, scaler = dp.get_features_and_scaler()
    companies_features = queries.get_companies_features()
    default_profile = dp.generate_default_user_profile(companies_features)
    default_profile.update(user_values)
    profile_features = dp.create_user_profile(default_profile, features_acc, dp.numerical_cols, scaler)
    recommendation_ids = rec.get_recommendations(profile_features, features_acc, default_profile, 5)
    
    if len(recommendation_ids) == 0:
        raise HTTPException(status_code=404, detail="No recommendations found")
    
    account = queries.get_account_data()
    recommendations = account[account.ID.isin(recommendation_ids)]
    transformed_data = dp.transform_api_response(recommendations)
    return transformed_data
