from pydantic import BaseModel, Field, conint
from typing import List, Dict


class CalculationRequest(BaseModel):
    """Schema for POST /calculate-partners"""
    total_leaders: conint(ge=1)
    total_followers: conint(ge=1)
    dance_styles: List[str]
    leader_knowledge: Dict[str, List[str]]
    follower_knowledge: Dict[str, List[str]]
    dance_duration_minutes: conint(ge=1)


class CalculationResponse(BaseModel):
    """Schema for the response of POST /calculate-partners"""
    average_dance_partners: float
