# 🚀 Deployment Guide

This guide shows how to deploy your Flask CI/CD application using Render.

## 📋 Prerequisites

- GitHub repository with CI/CD pipeline
- Render account (free tier available)

## 🎯 Deployment with Render

### Option 1: Automatic Deployment via GitHub Actions (Recommended)

1. **Sign up at [Render.com](https://render.com)**
2. **Create a new Web Service:**
   - Connect your GitHub repository
   - Choose "Web Service"
   - Select your repository and branch (main)

3. **Configure the service:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app.main:app --bind 0.0.0.0:$PORT`
   - **Python Version:** 3.11.5

4. **Get your Render credentials:**
   - Go to Render Dashboard → Account Settings → API Keys
   - Create a new API key
   - Copy your service ID from the service settings

5. **Add secrets to GitHub:**
   - Go to your GitHub repo → Settings → Secrets and variables → Actions
   - Add these secrets:
     - `RENDER_API_KEY`: Your Render API key
     - `RENDER_SERVICE_ID`: Your service ID

6. **Deploy automatically:**
   - Push to main branch
   - GitHub Actions will run tests
   - If tests pass, automatic deployment to Render

### Option 2: Manual Deployment to Render

1. **Go to [Render.com](https://render.com)**
2. **Create new Web Service**
3. **Connect your GitHub repository**
4. **Configure settings:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app.main:app --bind 0.0.0.0:$PORT`
   - **Python Version:** 3.11.5
5. **Deploy manually**

## 🔧 Configuration Files

### Procfile
```
web: gunicorn app.main:app --bind 0.0.0.0:$PORT
```

### render.yaml
```yaml
services:
  - type: web
    name: flask-ci-cd-demo
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app.main:app --bind 0.0.0.0:$PORT
    envVars:
      - key: FLASK_ENV
        value: production
      - key: PYTHON_VERSION
        value: 3.11.5
```

## 🧪 Testing Your Deployment

1. **Health Check:** `GET /health`
2. **API Test:** `POST /square` with `{"number": 5}`
3. **Home Page:** `GET /`

## 🔄 CI/CD Flow

1. **Push code** → GitHub
2. **GitHub Actions** → Run tests
3. **If tests pass** → Deploy to production
4. **If tests fail** → Stop deployment

## 🛠️ Environment Variables

Set these in your deployment platform:
- `FLASK_ENV=production`
- `PORT=5000` (or let platform assign)

## 📊 Monitoring

- Check deployment logs in your platform dashboard
- Monitor health endpoint: `/health`
- Set up alerts for deployment failures
