from fastapi import FastAPI, HTTPException
from .models import CalculationRequest, CalculationResponse
from .simulation import simulate_event


app = FastAPI(title="Dance Partner Calculator API")

@app.post("/calculate-partners", response_model=CalculationResponse)
def calculate_partners(req: CalculationRequest):
    """ Calculate the average number of dance partners based on the provided request.

    This function validates the input data to ensure that the number of leaders and followers
    matches the size of their respective knowledge lists. If the validation passes, it simulates
    the event to calculate the average number of dance partners.

        req (CalculationRequest): An object containing the total number of leaders, total number 
                                  of followers, and their respective knowledge levels.

        HTTPException: If the total number of leaders does not match the size of the leader_knowledge list.
        HTTPException: If the total number of followers does not match the size of the follower_knowledge list.

        CalculationResponse: An object containing the average number of dance partners.
    """
    if req.total_leaders != len(req.leader_knowledge):
        raise HTTPException(status_code=400, detail="total_leaders does not match leader_knowledge size")
    if req.total_followers != len(req.follower_knowledge):
        raise HTTPException(status_code=400, detail="total_followers does not match follower_knowledge size")

    average = simulate_event(req)
    return CalculationResponse(average_dance_partners=average)
