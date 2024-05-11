FROM python:3.12-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip setuptools && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]