import os
import logging
from logging.handlers import SysLogHandler
from flask import Flask, request
import requests

app = Flask(__name__)

# Set up Logstash logging
LOGSTASH_HOST = os.getenv('LOGSTASH_HOST', 'localhost')
LOGSTASH_PORT = os.getenv('LOGSTASH_PORT', 5044)

log_handler = SysLogHandler(address=(LOGSTASH_HOST, int(LOGSTASH_PORT)))
formatter = logging.Formatter('%(asctime)s %(name)s: %(levelname)s %(message)s')
log_handler.setFormatter(formatter)

app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def home():
    app.logger.info('Home page accessed')
    return "Hello, DevOps Exam!"

@app.route('/db-test')
def test_db_connection():
    try:
        response = requests.get(f"http://{os.getenv('DATABASE_URL')}/db-test")
        response.raise_for_status()
        app.logger.info(f"DB test passed with status {response.status_code}")
        return f"DB test passed with status {response.status_code}"
    except requests.exceptions.RequestException as e:
        app.logger.error(f"DB test failed: {e}")
        return f"DB test failed: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)