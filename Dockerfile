
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install flask psycopg2-binary

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
