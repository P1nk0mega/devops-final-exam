# 📖 API Documentation for Flask App

## **1️⃣ Home Route**
- **Endpoint:** `/`
- **Method:** `GET`
- **Response:** `"Hello, DevOps Exam!"`

## **2️⃣ Database Connection Test**
- **Endpoint:** `/db-test`
- **Method:** `GET`
- **Response:** `"Database Connected Successfully!"` (if successful)
- **Error Response:** `"Database Connection Failed: <error_message>"` (if failed)

## **3️⃣ Logging & Monitoring**
- Logs are available using:
  ```sh
  docker logs flask-app
