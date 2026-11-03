import requests
from deep_translator import GoogleTranslator

articles_data = []  # List to store all article info

# -----------------------------
# API Key and URL
# -----------------------------
api_key = "pub_f7840226192c40ff84eaf54f39aec9e6"  # Replace with your API key from NewsData.io
url = "https://newsdata.io/api/1/news"

# -----------------------------
# User input for category and language
# -----------------------------
print("Enter a news category (e.g., business, entertainment, politics, science, sports, technology):")
category = input("Category: ").strip().lower()

print("Enter the target language code for translation (e.g., en for English, hi for Hindi, mr for Marathi):")
target_lang = input("Language code: ").strip().lower()

# -----------------------------
# Parameters for the API request
# -----------------------------
params = {
    "apikey": api_key,
    "country": "in",      # 'in' for India
    "language": "en",     # Original language of news
    "category": category  # User-chosen category
}

# -----------------------------
# Send GET request to NewsData.io API
# -----------------------------
response = requests.get(url, params=params)

# -----------------------------
# Check the response
# -----------------------------
if response.status_code == 200:
    data = response.json()
    articles = data.get('results', [])  # Get list of news articles

    print(f"\n📰 Top {category.title()} News from India translated to {target_lang}\n" + "="*50 + "\n")

    if not articles:
        print("No news found.")
    else:
        for i, article in enumerate(articles, start=1):
            title = article.get('title', 'N/A')
            description = article.get('description', 'N/A')
            link = article.get('link', 'N/A')
            source = article.get('source_id', 'N/A')
            pub_date = article.get('pubDate', 'N/A')

            try:
                # Translate title and description
                translated_title = GoogleTranslator(source='auto', target=target_lang).translate(title) if title != 'N/A' else 'N/A'
                translated_desc = GoogleTranslator(source='auto', target=target_lang).translate(description) if description != 'N/A' else 'N/A'
            except Exception as e:
                translated_title = "Translation error"
                translated_desc = "Translation error"

            articles_data.append({
                "title": translated_title,
                "description": translated_desc,
                "link": link,
                "source": source,
                "published_at": pub_date
            })


            


else:
    print("Failed to fetch news.")
    print("Status Code:", response.status_code)
    print("Error:", response.text)

for i, article in enumerate(articles_data, start=1):
    print(f"Article {i}:")
    print("Title       :", article['title'])
    print("Description :", article['description'])
    print("Link        :", article['link'])
    print("Source      :", article['source'])
    print("Published At:", article['published_at'])
    print("-" * 50)
