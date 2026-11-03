import requests
from deep_translator import GoogleTranslator

# Your NewsAPI key
api_key = "665f9b1299b7475e9ca103b4bc8b1888"

# Get user inputs
print("Choose a category from the following options:")
print("business, entertainment, general, health, science, sports, technology")
category = input("Enter category: ").strip().lower()

print("Enter the target language code for translation (e.g., en for English, hi for Hindi, mr for Marathi):")
target_lang = input("Enter language code: ").strip().lower()

# Build the API URL
url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}"

# Send the request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    articles = data.get('articles', [])

    if not articles:
        print("No articles found.")
    else:
        print(f"\nTop {category.title()} News translated to {target_lang}:\n")
        
        for i, article in enumerate(articles, start=1):
            title = article.get('title', 'N/A')
            description = article.get('description', 'N/A')
            url_link = article.get('url', 'N/A')

            # Translate title and description
            translated_title = GoogleTranslator(source='auto', target=target_lang).translate(title) if title != 'N/A' else 'N/A'
            translated_desc = GoogleTranslator(source='auto', target=target_lang).translate(description) if description != 'N/A' else 'N/A'

            print(f"Article {i}:")
            print("Title       :", translated_title)
            print("Description :", translated_desc)
            print("URL         :", url_link)
            print("-"*50)
else:
    print("Failed to fetch news. Error code:", response.status_code)