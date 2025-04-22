from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

API_KEY = "1dd3d77bda7343d59e448a2a51814b12"  # Use your NewsAPI key

@app.route('/', methods=['GET', 'POST'])
def home():
    articles = []
    if request.method == 'POST':
        topic = request.form['topic']
        one_month_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        url = f"https://newsapi.org/v2/everything?q={topic}&from={one_month_ago}&sortBy=publishedAt&apiKey={API_KEY}"
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get("articles", [])
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
