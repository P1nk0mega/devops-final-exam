# 🔄 CI/CD Pipeline - DevOps Final Exam

## **📌 Overview**
The CI/CD pipeline is automated using **GitHub Actions**:
- ✅ Runs tests on every push to `main`
- ✅ Builds & pushes Docker image to **Docker Hub**
- ✅ Deploys the app to a **remote server** automatically

## **📂 GitHub Actions Workflow**
Located in `.github/workflows/ci-cd-pipeline.yml`.

### **Pipeline Steps**
1️⃣ **Checkout Code**
```yaml
- name: Checkout Code
  uses: actions/checkout@v3
