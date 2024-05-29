from pydantic import BaseModel

class UserProfile(BaseModel):
    RATING: str
    HQ_LOCATION__C: str
    INDUSTRY: str
    OWNERSHIP: str
    TYPE_ACC: str
    OWNER_INTENT_TO_SELL__C: int


