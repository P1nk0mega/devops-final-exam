
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install flask psycopg2-binary pytest requests

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl --fail http://localhost:5000 || exit 1

CMD ["python", "app.py"]
