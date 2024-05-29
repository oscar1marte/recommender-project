from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(profile_features, features, user_values, top_n=5):
    profile_similarity = cosine_similarity(profile_features, features[user_values.keys()])
    similarity_scores = list(enumerate(profile_similarity[0]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_indices = [idx for idx, score in similarity_scores[:top_n]]
    return features.iloc[top_indices]['ID_ACC'].values
