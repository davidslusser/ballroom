## Installing Dependencies
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```


## Running The App Locally
```
uvicorn app.main:app --reload
```

You’ll now see the live docs at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc


## Running Tests
```
pytest tests
```


## Repository Structure
```
ballroom/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app entry point
│   ├── models.py          # Pydantic request/response models
│   ├── simulation.py      # Business logic (partner simulation)
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py        # Integration tests
│   └── test_simulation.py # Unit tests for simulation logic
│
├── requirements.txt       # Dependency list for pip
├── README.md              # (Optional) Challenge summary or instructions
```

<br/>

## Using Docker

### Build the Docker Image
```docker build -t ballroom .```


### Run the Container
```docker run -d -p 8000:8000 --name ballroom-container ballroom```

Then visit:
 - http://localhost:8000/docs → for the Swagger UI
 - http://localhost:8000/redoc → for the Redoc


### To Stop the Container:
```docker stop ballroom-container```

### To Remove the Container:
```docker rm ballroom-container```

