import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

def predict_trends(data: pd.DataFrame):
    required_columns = ['impressions', 'clicks', 'spend', 'conversions']
    
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"Input DataFrame must contain columns: {required_columns}")

    X = data[['impressions', 'clicks', 'spend']]
    y = data['conversions']

    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)
    score = r2_score(y, predictions)

    return predictions, score
