
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_meta_ads_data(days=30):
    today = datetime.today()
    data = []
    for i in range(days):
        date = today - timedelta(days=i)
        impressions = random.randint(1000, 10000)
        clicks = random.randint(50, impressions // 10)
        spend = round(random.uniform(10, 200), 2)
        conversions = random.randint(0, clicks // 2)
        ctr = clicks / impressions if impressions > 0 else 0
        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'impressions': impressions,
            'clicks': clicks,
            'spend': spend,
            'conversions': conversions,
            'ctr': round(ctr, 4)
        })
    return pd.DataFrame(data)
