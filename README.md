# Dance Partner Calculator API - Python

A lightweight FastAPI service that estimates the average number of unique dance partners each participant will meet at a ballroom event, given their dance‑style knowledge and event duration.

### Features

- Single POST endpoint/calculate-partners
- Input validation with Pydantic
- Auto-generated Swagger UI & ReDoc docs (FastAPI default)
- Fully tested with pytest (edge-cases included)
- Container-ready via a minimal Dockerfile

### Project Structure
```
ballroom/
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI entrypoint & endpoint
│   ├── models.py           # Pydantic request/response models
│   └── simulation.py       # Partner-matching logic
├── sample_payloads/        # Sample JSON payloads for manual verification
├── tests/                  # Unit & integration tests
│   ├── __init__.py
│   ├── test_api.py         # Api tests
│   └── test_simulation.py  # Partner-matching tests
├── requirements.txt        # Python dependencies (plain pip)
├── Dockerfile              # Container build recipe
├── LICENSE                 # Repo license
└── README.md               # Project documentation (this file)
```

<br/>

## Local Setup

### Clone & enter project
```
$ git clone git@github.com:davidslusser/ballroom.git ballroom
$ cd ballroom
```

### Create & activate a virtual environment
```
$ python -m venv venv
$ source venv/bin/activate          # Windows: venv\Scripts\activate
```

### Install dependencies
```
(venv) $ pip install -r requirements.txt
```


### Run the server (auto-reload)
```
(venv) $ uvicorn app.main:app --reload
```

- Visit http://localhost:8000/docs for the Swagger UI.
- Visit http://localhost:8000/redoc for the ReDoc UI.

### Running Unittests
```
(venv) $ pytest -q
```

<br/>

## Docker Usage

### Build the image
```docker build -t ballroom .```

### Run the container
```docker run -d -p 8000:8000 --name ballroom ballroom```

Then visit:
 - http://localhost:8000/docs → for the Swagger UI
 - http://localhost:8000/redoc → for the Redoc UI

### To Stop the Container:
```docker stop ballroom```

### To Remove the Container:
```docker rm ballroom```