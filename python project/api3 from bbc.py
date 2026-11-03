import requests

# -----------------------------
# NewsAPI Key and URL
# -----------------------------
api_key = "665f9b1299b7475e9ca103b4bc8b1888"  # Replace with your API key if needed
url = "https://newsapi.org/v2/top-headlines"

# -----------------------------
# Parameters for the API request
# -----------------------------
params = {
    "sources": "bbc-news",
    "apiKey": api_key
}

# -----------------------------
# Send GET request to NewsAPI
# -----------------------------
response = requests.get(url, params=params)

# -----------------------------
# Check response status
# -----------------------------
if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python dict
    print("\n📰 Top BBC News Headlines:\n" + "="*50 + "\n")
    
    for i, article in enumerate(data.get('articles', []), start=1):
        print(f"Article {i}:")
        print("Title       :", article.get('title', 'N/A'))
        print("Description :", article.get('description', 'N/A'))
        print("URL         :", article.get('url', 'N/A'))
        print("Image URL   :", article.get('urlToImage', 'N/A'))
        print("Published At:", article.get('publishedAt', 'N/A'))
        print("-"*50)
else:
    print("Error fetching news. Status Code:", response.status_code)
    print("Response:", response.text)
