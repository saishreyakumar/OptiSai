# Dummy trend model
import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_trends(data):
    model = LinearRegression()
    X = data[['impressions']]
    y = data['conversions']
    model.fit(X, y)
    return model.predict(X)
