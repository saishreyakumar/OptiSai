
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_shopify_sales_data(days=30):
    today = datetime.today()
    data = []
    for i in range(days):
        date = today - timedelta(days=i)
        orders = random.randint(5, 50)
        avg_order_value = round(random.uniform(20.0, 150.0), 2)
        total_sales = round(orders * avg_order_value, 2)
        new_customers = random.randint(1, orders)
        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'orders': orders,
            'avg_order_value': avg_order_value,
            'total_sales': total_sales,
            'new_customers': new_customers
        })
    return pd.DataFrame(data)
