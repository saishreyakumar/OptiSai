# OptiSai – AI-Powered Marketing Optimization Platform

OptiSai is a proof-of-concept platform designed to optimize Meta Ads performance using machine learning, simulated Meta and Shopify APIs, and a modern full-stack interface. It analyzes advertising and sales data to provide actionable insights, track ROI, and recommend A/B tests and budget adjustments.

---

## Features

### Core Capabilities

- Simulated **Meta Ads API**: Impressions, spend, CTR, conversions
- Simulated **Shopify API**: Sales, customer behavior, order values
- **Trend analysis** using linear regression
- **ROI tracking** and visualizations
- **Daily performance recommendations**
- **A/B test suggestions** for creatives and audiences
- **Expandable chart dashboard** built with Bootstrap + Chart.js

### Dashboard Insights

- CTR over time
- Sales over time
- ROI tracking
- Daily insights panel
- Dedicated A/B test suggestion panel

---

## Project Structure

```
optisai/
├── backend/
│   ├── api/                # Flask application routes
│   ├── models/             # ML model logic (trend prediction)
│   └── utils/              # Mock data generators and recommendations
│
├── frontend/
│   ├── static/             # JS, CSS (if needed)
│   └── templates/          # index.html dashboard template
├── notebooks/              # EDA scripts (optional)
├── scripts/                # Placeholder for future automation
└── requirements.txt        # Python dependencies
```

---

## Tech Stack

- **Frontend**: HTML5, Bootstrap 5, Chart.js
- **Backend**: Python, Flask
- **ML**: Scikit-learn (LinearRegression)
- **Mock Data**: Custom generators (no real tokens required)
- **Deployment**: Locally runnable via Flask

---

## Setup Instructions

1. **Clone the repository / unzip the folder**
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   export FLASK_APP=backend.api.app
   flask run
   ```

Visit: `http://localhost:5000`

---
