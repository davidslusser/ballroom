###############################################################################
# ---------- 1️⃣  Build stage: compile wheels & collect pure‑Python deps ------
###############################################################################
FROM python:3.11-slim AS builder

# 1. Install *native* build tools only here
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /install

# 2. Copy dependency list first for better Docker‑layer caching
COPY requirements.txt .

# 3. Build wheels into /wheels, then install into /install
RUN pip wheel --wheel-dir /wheels -r requirements.txt \
 && pip install --prefix=/install --no-deps /wheels/*

###############################################################################
# ---------- 2️⃣  Runtime stage: copy deps & app, no compilers ---------------
###############################################################################
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# 4. Copy site‑packages from the builder (≈ /usr/local or /install)
COPY --from=builder /install /usr/local

# 5. Copy app source
COPY app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
