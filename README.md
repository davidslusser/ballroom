# Dance Partner Calculator API - Python

A lightweight API service that estimates the average number of unique dance partners each participant will meet at a ballroom event, given their dance‑style knowledge and event duration.

### Tech Stack

**Primary Language:** Python  
**Web Framework:** FastAPI  
**ASGI Server:** Uvicorn  
**Data Modelling:** Pydantic

**Python**  
Python is a high-level, interpreted programming language known for its readability, simplicity, and versatility. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. With a rich ecosystem of libraries and frameworks, Python is widely used in web development, data science, automation, machine learning, and more.

**FastAPI**  
FastAPI is a modern, high-performance web framework for building APIs with Python, designed for speed and ease of use. It automatically generates interactive API documentation with Swagger UI and ReDoc, and supports asynchronous programming (async/await) for handling high-concurrency scenarios. Leveraging Python type hints, FastAPI provides automatic validation, ensuring data integrity with minimal effort.

**Uvicorn**  
Uvicorn is a fast, asynchronous web server for Python, designed to run ASGI-compatible applications like FastAPI and Starlette. It supports both HTTP and WebSocket protocols, making it ideal for real-time applications. Built on uvloop and httptools, Uvicorn offers high performance with low latency and is commonly used for development and production environments.

**Pydantic**  
Pydantic is a data validation and parsing library for Python, built on top of Python's type hints. It allows you to define data models with strong typing, and automatically validates and converts input data (e.g., from JSON or forms). Pydantic ensures data integrity by raising errors when data doesn't match the specified types, making it ideal for APIs and configurations.


### Application Features

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
├── sample_payloads/        # Sample JSON payloads for verification/testing
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

## Local Setup and Development

### Clone & enter project
```
$ git clone git@github.com:davidslusser/ballroom.git ballroom
$ cd ballroom
```

### Create & activate a virtual environment
```
$ python -m venv venv
$ source venv/bin/activate     # Windows: venv\Scripts\activate
```

### Install dependencies
```
(venv) $ pip install -r requirements.txt
```


### Running the server (auto-reload)
```
(venv) $ uvicorn app.main:app --reload
```

- Visit http://localhost:8000/docs for the Swagger UI.
- Visit http://localhost:8000/redoc for the ReDoc UI.

### Running Unittests
```
(venv) $ pytest 
```

<br/>

## Docker Usage

### Build the image
```docker build -t ballroom .```

### Run the container
```docker run -d -p 8000:8000 --name ballroom ballroom```

Then visit:
 - http://localhost:8000/docs for the Swagger UI
 - http://localhost:8000/redoc for the Redoc UI

### To Stop the Container:
```docker stop ballroom```

### To Remove the Container:
```docker rm ballroom```

<br/>

## Calling the API

Run the app directly or using Docker following the instructions above.

Send a POST request to the server, via curl (or similar means) such as:

```
curl --location 'http://localhost:8000/calculate-partners' \
--header 'Content-Type: application/json' \
--data '{
    "total_leaders": 1,
    "total_followers": 1,
    "dance_styles": ["Waltz"],
    "leader_knowledge": {
      "1": ["Waltz"]
    },
    "follower_knowledge": {
      "A": ["Waltz"]
    },
    "dance_duration_minutes": 15
  }
  '
```

Sample payloads are provided (in the sample_payloads directory) for manual testing.

