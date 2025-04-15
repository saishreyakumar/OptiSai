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
│   ├── api/
│   │   └── app.py                     # Flask API entry point and route handlers
│   ├── models/
│   │   └── trend_model.py             # Simple linear regression model for trends
│   └── utils/
│       ├── meta_ads_mock.py           # Mock Meta Ads data generator
│       ├── shopify_mock.py            # Mock Shopify sales data generator
│       └── recommendations.py         # ROI/CTR-based insights & A/B test suggestions
├── frontend/
│   └── templates/
│       └── index.html                 # Responsive dashboard using Bootstrap & Chart.js
│
├── Dockerfile                         # Docker for deployment
├── render.yaml                        # Render.com deployment configuration
├── requirements.txt                   # Download needed libraries
├── README.md                          # A Readme doc for better understanding
├── Architecture_diagram.png           # Architecture diagram


```

---

## Tech Stack

- **Frontend**: HTML5, Bootstrap 5, Chart.js
- **Backend**: Python, Flask
- **ML**: Scikit-learn (LinearRegression)
- **Mock Data**: Custom generators (no real tokens required)
- **Deployment**: Locally runnable via Flask or hosted using Docker/Render

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

## Deployment (Docker + Render)

### Using Docker (local or cloud-based)

```bash
docker build -t optisai .
docker run -p 10000:10000 optisai
```

Visit: `http://localhost:10000`
