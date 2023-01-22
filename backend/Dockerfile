FROM python:alpine

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn","routes:app"]