FROM python:3.12-slim

WORKDIR /app

COPY src/ /app/src
COPY requirements.pip /app/requirements.pip

RUN pip install -r requirements.pip

CMD ["fastapi", "run", "app/main.py", "--port", "80"]