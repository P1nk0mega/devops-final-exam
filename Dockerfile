FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN adduser --disabled-password appuser
USER appuser

COPY . .

CMD ["python", "app.py"]
