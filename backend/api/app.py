
from flask import Flask, render_template, jsonify
import os
from backend.utils.meta_ads_mock import generate_meta_ads_data
from backend.utils.shopify_mock import generate_shopify_sales_data

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/meta_ads')
def meta_ads_api():
    df = generate_meta_ads_data()
    return df.to_json(orient='records')

@app.route('/api/shopify')
def shopify_api():
    df = generate_shopify_sales_data()
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)

from backend.utils.recommendations import generate_recommendations

@app.route('/api/recommendations')
def recommendations_api():
    meta_df = generate_meta_ads_data()
    shopify_df = generate_shopify_sales_data()
    recs = generate_recommendations(meta_df, shopify_df)
    return jsonify(recs)
