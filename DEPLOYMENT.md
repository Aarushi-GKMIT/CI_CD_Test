# 🚀 Deployment Guide

This guide shows how to deploy your Flask CI/CD application using different platforms.

## 📋 Prerequisites

- GitHub repository with CI/CD pipeline
- Account on your chosen deployment platform

## 🎯 Deployment Options

### Option 1: Railway (Recommended - Free)

1. **Sign up at [Railway.app](https://railway.app)**
2. **Connect your GitHub repository**
3. **Get your Railway credentials:**
   - Go to Railway Dashboard → Your Project → Settings
   - Copy your `RAILWAY_TOKEN` and `RAILWAY_SERVICE_ID`

4. **Add secrets to GitHub:**
   - Go to your GitHub repo → Settings → Secrets and variables → Actions
   - Add these secrets:
     - `RAILWAY_TOKEN`: Your Railway token
     - `RAILWAY_SERVICE_ID`: Your service ID

5. **Deploy automatically:**
   - Push to main branch
   - GitHub Actions will run tests
   - If tests pass, automatic deployment to Railway

### Option 2: Heroku

1. **Install Heroku CLI**
2. **Create Heroku app:**
   ```bash
   heroku create your-app-name
   ```

3. **Update workflow for Heroku:**
   ```yaml
   - name: Deploy to Heroku
     uses: akhileshns/heroku-deploy@v3.12.12
     with:
       heroku_api_key: ${{secrets.HEROKU_API_KEY}}
       heroku_app_name: "your-app-name"
       heroku_email: "your-email@example.com"
   ```

### Option 3: Render

1. **Sign up at [Render.com](https://render.com)**
2. **Connect GitHub repository**
3. **Configure build settings:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app.main:app --bind 0.0.0.0:$PORT`

## 🔧 Configuration Files

### Procfile
```
web: gunicorn app.main:app --bind 0.0.0.0:$PORT
```

### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn app.main:app --bind 0.0.0.0:$PORT",
    "healthcheckPath": "/health",
    "healthcheckTimeout": 100
  }
}
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
