FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY app.py .

COPY templates/ ./templates/

EXPOSE 8080

CMD ["python3","app.py"]






