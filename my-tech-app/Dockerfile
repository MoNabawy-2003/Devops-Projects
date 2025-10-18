FROM python:3.9-slim

WORKDIR /app

COPY my-tech-app/app/requirements.txt .

RUN pip install -r requirements.txt

COPY my-tech-app/app/ .

EXPOSE 5000

CMD ["python", "app.py"]
