import logging
import os
from flask import Flask
import psycopg2

app = Flask(__name__)

LOGSTASH_HOST = os.getenv("LOGSTASH_HOST", "logstash")
LOGSTASH_PORT = int(os.getenv("LOGSTASH_PORT", 5044))

logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_handler = logging.handlers.SysLogHandler(address=(LOGSTASH_HOST, LOGSTASH_PORT))
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

@app.route("/")
def home():
    logger.info("Accessed home route")
    return "Hello, DevOps Exam!"

@app.route("/db-test")
def db_test():
    logger.info("Database test route hit")
    return "Database Connected Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
