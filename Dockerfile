
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install flask psycopg2-binary
RUN pip install -r requirements.txt

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
