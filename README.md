# 🛒 E-Commerce DevOps Project


## 📌 Project Description

A Flask-based e-commerce web application that demonstrates a **complete DevOps CI/CD pipeline** including version control, automated builds, testing, static code analysis, containerisation, and cloud deployment.

**Live URL:** https://ecommerce-devops-project.onrender.com

---

## 🚀 Features

- User authentication (Login & Signup with validation)
- Product listing and product detail pages
- Search functionality
- Shopping cart (add / remove items)
- Checkout with order confirmation
- Contact page
- Responsive UI with HTML & CSS

---

## ⚙️ CI/CD Pipeline Architecture

```
Developer Push (GitHub)
        │
        ▼
GitHub Actions Triggered
        │
        ├── Job 1: Build & Test
        │       ├── Install dependencies
        │       ├── Run Flake8 (Static Code Analysis)
        │       ├── Run Pytest + Coverage Report
        │       └── Upload test artifacts
        │
        ├── Job 2: Docker Build
        │       ├── Build Docker image
        │       └── Smoke test container
        │
        └── Job 3: Deploy to Render (on main push only)
                └── Trigger Render deploy hook
```

---

## 🛠️ Tools & Technologies

| Category            | Tool / Technology        |
|---------------------|--------------------------|
| Version Control     | Git, GitHub              |
| CI/CD               | GitHub Actions           |
| Programming         | Python 3.10, Flask       |
| Testing             | Pytest, pytest-cov       |
| Static Analysis     | Flake8                   |
| Containerisation    | Docker                   |
| Cloud Deployment    | Render.com               |
| Build Tool          | pip, gunicorn            |

---

## 📂 Project Structure

```
ecommerce-devops-project/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml          ← GitHub Actions CI/CD pipeline
│
├── demo_ecommerce/
│   ├── app.py                 ← Main Flask application
│   ├── __init__.py
│   ├── templates/             ← HTML templates
│   └── static/style.css       ← Stylesheet
│
├── tests/
│   └── test_app.py            ← Pytest test suite (35+ tests)
│
├── Dockerfile                 ← Docker containerisation
├── render.yaml                ← Render cloud deploy config
├── requirements.txt           ← Python dependencies
├── pytest.ini                 ← Test configuration
├── Jenkinsfile                ← Jenkins pipeline (alternative CI)
├── .gitignore
└── README.md
```

---

## ▶️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/tejalkunde/ecommerce-devops-project.git
cd ecommerce-devops-project

# 2. Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Run the application
python demo_ecommerce/app.py

# 4. Open in browser
# http://127.0.0.1:5000
```

---

## 🐳 Run with Docker

```bash
# Build the image
docker build -t ecommerce-flask .

# Run the container
docker run -d -p 5000:5000 --name ecommerce-container ecommerce-flask

# Open browser at http://localhost:5000
```

---

## 🧪 Run Tests

```bash
# Run all tests with coverage
pytest tests/ --cov=demo_ecommerce --cov-report=term-missing -v

# Run with XML report (for CI)
pytest tests/ --junitxml=report.xml
```

---

## 🔍 Static Code Analysis

```bash
flake8 demo_ecommerce/app.py tests/test_app.py --max-line-length=120
```

---

## ☁️ Deployment (Render)

1. Connect your GitHub repo to [render.com](https://render.com)
2. Create a **Web Service**
3. Set **Build Command:** `pip install -r requirements.txt`
4. Set **Start Command:** `gunicorn demo_ecommerce.app:app --bind 0.0.0.0:$PORT`
5. Add `RENDER_DEPLOY_HOOK_URL` as a GitHub secret for auto-deploy on push

---

## 🌿 Branching Strategy

| Branch  | Purpose                          |
|---------|----------------------------------|
| `main`  | Production-ready, triggers deploy|
| `dev`   | Development and feature testing  |

Pull requests from `dev` → `main` trigger full CI pipeline before merge.

---

## 👥 Contributors

- Tejal Kunde
- Rutuja Narode
- Shreya Dubey
- Eshwari Borade

---

## 📋 Submitted To

**Prof. Shipha Pant** | DevOps T1 Mini Project | 25 Marks
