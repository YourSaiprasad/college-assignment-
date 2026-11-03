import requests

# -----------------------------
# API Key and URL
# -----------------------------
api_key = "pub_f7840226192c40ff84eaf54f39aec9e6"  # Replace with your API key from NewsData.io
url = "https://newsdata.io/api/1/news"

# -----------------------------
# Parameters for the API request
# -----------------------------
params = {
    "apikey": api_key,
    "country": "in",      # 'in' for India
    "language": "en"      # Get English news
}

# -----------------------------
# Send GET request to NewsData.io API
# -----------------------------
response = requests.get(url, params=params)

# -----------------------------
# Check the response
# -----------------------------
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    articles = data.get('results', [])  # Get list of news articles

    print("\n📰 Top News from India\n" + "="*50 + "\n")

    if not articles:
        print("No news found.")
    else:
        for i, article in enumerate(articles, start=1):
            print(f"Article {i}:")
            print("Title       :", article.get('title', 'N/A'))
            print("Description :", article.get('description', 'N/A'))
            print("Link        :", article.get('link', 'N/A'))
            print("Source      :", article.get('source_id', 'N/A'))
            print("Published At:", article.get('pubDate', 'N/A'))
            print("-"*50)

else:
    print("Failed to fetch news.")
    print("Status Code:", response.status_code)
    print("Error:", response.text)
