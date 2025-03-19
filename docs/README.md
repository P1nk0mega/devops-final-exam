# 🚀 DevOps Final Exam Project

![Docker](https://img.shields.io/badge/Docker-✔-blue) 
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-green) 
![Monitoring](https://img.shields.io/badge/Monitoring-Prometheus_&_Grafana-yellow) 
![Logging](https://img.shields.io/badge/Logging-Fluentd-red) 
![Security](https://img.shields.io/badge/Security-✔-blueviolet)

## 📖 Project Overview
This project is a **Dockerized web application** using **Flask** as the backend and **PostgreSQL** as the database. It is **fully automated** with a CI/CD pipeline, monitoring, logging, and security best practices.

## 🎯 Features & Technologies Used

✅ **Infrastructure as Code** (Docker, Docker Compose)  
✅ **Automated CI/CD pipeline** (GitHub Actions)  
✅ **Dockerized Web App** (Flask + PostgreSQL)  
✅ **Multiple Containers** (Backend + DB + Monitoring + Logging)  
✅ **Security Best Practices** (Non-root user, Secrets in `.env`, Private Network)  
✅ **Automated Deployment** (Ansible Playbook)  
✅ **Monitoring & Alerts** (Prometheus & Grafana)  
✅ **Centralized Logging** (Fluentd)  
✅ **Unit & Deployment Testing**  

---

## 🏗️ Project Structure
```
devops-final-exam/
│── app/                     # Flask Web Application
│   ├── app.py               # Main application file
│   ├── requirements.txt      # Dependencies
│   ├── Dockerfile            # Docker setup for Flask app
│── infra/                    # Infrastructure setup
│   ├── docker-compose.yml     # Service definitions
│── monitoring/               # Monitoring setup
│   ├── prometheus.yml        # Prometheus config
│── logs/                     # Logging setup
│   ├── fluentd.conf          # Fluentd config
│── ci-cd/                    # CI/CD Pipeline setup
│   ├── deploy.yml            # Ansible deployment script
│── tests/                    # Testing setup
│   ├── test_app.py           # Unit tests for Flask app
│── docs/                     # Documentation
│   ├── README.md             # Project Documentation
│── .env                      # Environment Variables
│── .gitignore                # Git Ignore file
│── ansible.cfg               # Ansible Configuration
```

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/P1nk0mega/devops-final-exam.git
cd devops-final-exam
```

### **2️⃣ Setup Environment Variables**
Create a `.env` file:
```sh
nano .env
```
Paste the following:
```ini
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydb
```
Save and exit.

### **3️⃣ Build & Run the Application**
```sh
docker-compose up -d --build
```

---

## 🚀 CI/CD Pipeline (GitHub Actions)
A **GitHub Actions** workflow automatically:
- **Builds** and **tests** the application.
- **Pushes** the Docker image to Docker Hub.
- **Deploys** the application using Ansible.

### **Trigger Deployment**
Push changes to the repository:
```sh
git add .
git commit -m "Deploying app"
git push origin main
```

---

## 📊 Monitoring Setup
The project includes **Prometheus** and **Grafana** for monitoring.

- **Prometheus** → [`http://localhost:9090`](http://localhost:9090)
- **Grafana** → [`http://localhost:3000`](http://localhost:3000) (Default: `admin/admin`)

---

## 📜 Logging Setup
Logs are centralized with **Fluentd**.

Check logs:
```sh
docker logs fluentd -f
```

---

## 🔐 Security Features
- **Runs as a non-root user** in Docker (`appuser`).
- **Database is isolated** in a private Docker network.
- **Sensitive data stored** in `.env` file.

---

## 🧪 Testing
Run unit tests:
```sh
python -m unittest discover tests
```

---

## 📌 Contributors
👤 **Elijus.K**  
📧 elijus1997@gmail.com  
💼 [LinkedIn] https://www.linkedin.com/in/elijus-kučikas-1a1061176/

---

🚀 **This README file contains everything needed for your DevOps exam submission!** 🔥
