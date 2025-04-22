import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv("NEWS_API_KEY")

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
