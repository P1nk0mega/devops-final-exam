# 🚀 DevOps Final Exam - Flask App

## 📌 Overview
This is a simple **Flask-based web application** that demonstrates **CI/CD, monitoring, logging, and containerization** using **Docker & GitHub Actions**.

## ✅ Features
- Flask app with PostgreSQL database
- Fully Dockerized (works with `docker-compose`)
- CI/CD pipeline with **GitHub Actions**
- Automated testing using **pytest**
- Centralized logging using **logging module & Docker**
- Monitoring with **Prometheus & Grafana**

---

## 🔧 **Setup Instructions**

1️⃣ Clone the Repository**
```sh
git clone https://github.com/P1nk0mega/devops-final-exam.git
cd devops-final-exam

2️⃣ Deploy with Docker Compose**
```sh
docker --version
kubectl version --client

3️⃣ Verify the App**
```sh
curl http://localhost:5000

Expected output:
Hello, DevOps Exam!

Check database connectivity:
curl http://localhost:5000/db-test


📂 Project Structure

devops-final-exam/
│── app.py             # Flask app
│── Dockerfile         # Docker build file
│── docker-compose.yml # Multi-container setup
│── k8s/               # Kubernetes YAML manifests
│── requirements.txt   # Python dependencies
│── tests/             # Pytest test cases
│── .github/workflows/ # CI/CD pipeline
│── docs/              # Documentation folder
│── nginx.conf         # Reverse proxy configuration
│── logstash.conf      # Logstash configuration
│── README.md          # Project documentation


🔄 CI/CD Pipeline
This project uses GitHub Actions for automation: ✅ Run tests on every push
✅ Build & Push Docker image to Docker Hub
✅ Deploy Kubernetes services

GitHub Actions Workflow
Located in .github/workflows/ci-cd-pipeline.yml.

Pipeline Steps

1️⃣ Checkout Code
```sh
- name: Checkout Code
  uses: actions/checkout@v3

2️⃣ Run Tests
```sh
- name: Run Tests
  run: pytest tests/

3️⃣ Build & Push Docker Image
```sh
- name: Build and Push Docker Image
  run: |
    docker build -t yourdockerhubusername/devops-flask-app .
    docker tag yourdockerhubusername/devops-flask-app:latest
    docker push yourdockerhubusername/devops-flask-app:latest

📊 Monitoring & Logging
This project uses: ✅ Prometheus (for metrics)
✅ Grafana (for dashboards)
✅ ELK Stack (Elasticsearch, Logstash, Kibana) for centralized logging

📌 Access Monitoring Tools
Tool	    URL
Prometheus	http://localhost:9090
Grafana	    http://localhost:3000
Kibana	    http://localhost:5601


❓ Troubleshooting
1️⃣ How to Restart the App?

docker-compose restart
kubectl rollout restart deployment flask-app


2️⃣ How to View Logs?

docker logs flask-app

Or in Kibana:

curl -X GET "localhost:9200/flask-logs/_search?pretty"


3️⃣ How to Rebuild Everything?

docker-compose down
docker system prune -a -f
docker-compose up --build -d

🛠 Contributing

1️⃣ Fork the Repository
Click the Fork button on GitHub.

2️⃣ Clone Your Fork
git clone https://github.com/yourusername/devops-final-exam.git

3️⃣ Create a New Branch
git checkout -b feature-branch

4️⃣ Make Your Changes & Commit
git add .
git commit -m "Added a new feature"

5️⃣ Push to GitHub & Create a Pull Request
git push origin feature-branch
