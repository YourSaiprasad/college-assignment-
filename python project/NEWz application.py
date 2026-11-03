import tkinter as tk
import requests
from deep_translator import GoogleTranslator
import webbrowser

# ----------------- Global Variables -----------------
language = "English"
category = "sports"
articles_data = []

# ----------------- Functions -----------------

def on_category_click(cat):
    global category
    category = cat.lower()
    articles_data.clear()
    showNews()
    refresh_headlines()

def on_language_click(lang):
    global language
    language = lang
    info_label.config(text=f"Language selected: {lang}")
    articles_data.clear()
    showNews()
    refresh_headlines()

def showNews():
    lang_code_map = {
        "English": "en",
        "Hindi": "hi",
        "Marathi": "mr",
        "Spanish": "es",
        "French": "fr",
        "German": "de"
    }
    target_lang = lang_code_map.get(language, "en")
    
    # -----------------------------
    # API Key and URL
    # -----------------------------
    api_key = "pub_f7840226192c40ff84eaf54f39aec9e6"
    url = "https://newsdata.io/api/1/news"
    
    # -----------------------------
    # Parameters for the API request
    # -----------------------------
    params = {
        "apikey": api_key,
        "country": "in",
        "language": "en",
        "category": category
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

        if not articles:
            print("No news found.")
        else:
            for article in articles:
                title = article.get('title', 'N/A')
                description = article.get('description', 'N/A')
                link = article.get('link', 'N/A')
                source = article.get('source_id', 'N/A')
                pub_date = article.get('pubDate', 'N/A')

                try:
                    # Translate title and description
                    translated_title = GoogleTranslator(source='auto', target=target_lang).translate(title) if title != 'N/A' else 'N/A'
                    translated_desc = GoogleTranslator(source='auto', target=target_lang).translate(description) if description != 'N/A' else 'N/A'
                except:
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

def refresh_headlines():
    # Clear existing article widgets
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    # Iterate over each article and display all its data
    for i, article in enumerate(articles_data):
        align = "w" if i % 2 == 0 else "e"
        bg_color = "#ffffff" if i % 2 == 0 else "#ffebcc"

        # Frame for each article
        article_frame = tk.Frame(scrollable_frame, bg=bg_color, bd=1, relief="solid", padx=10, pady=10)
        article_frame.pack(fill="x", pady=5, padx=(0, 20) if i % 2 == 1 else (20, 0), anchor=align)

        # ---------- Title ----------
        title = article.get('title', 'No Title')
        title_label = tk.Label(article_frame, text=f"📰 {title}", font=("Helvetica", 14, "bold"),
                               bg=bg_color, fg="#222222", wraplength=550, justify="left")
        title_label.pack(anchor="w")

        # ---------- Description ----------
        description = article.get('description', '')
        if description and description != "N/A":
            desc_label = tk.Label(article_frame, text=description, font=("Arial", 11),
                                  bg=bg_color, fg="#333333", wraplength=550, justify="left")
            desc_label.pack(anchor="w", pady=5)

        # ---------- Source and Published Date ----------
        source = article.get('source', 'Unknown Source')
        pub_date = article.get('published_at', 'Unknown Date')
        meta_text = f"📅 Published: {pub_date}    🏢 Source: {source}"
        meta_label = tk.Label(article_frame, text=meta_text, font=("Arial", 10, "italic"),
                              bg=bg_color, fg="#666666")
        meta_label.pack(anchor="w")

        # ---------- Clickable Link ----------
        link = article.get('link', '')
        if link and link != 'N/A':
            def open_link(url=link):
                webbrowser.open_new_tab(url)

            link_label = tk.Label(article_frame, text="🔗 Read full article", font=("Arial", 10, "underline"),
                                  fg="blue", bg=bg_color, cursor="hand2")
            link_label.pack(anchor="w", pady=(5, 0))
            link_label.bind("<Button-1>", lambda e, url=link: open_link(url))

def start_now():
    info_label.config(text="Login Now button clicked!")

def learn_more():
    info_label.config(text="Logout button clicked!")

def nav_click(name):
    info_label.config(text=f"{name} clicked!")

# ----------------- Initial Fetch -----------------
showNews()

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("BL.S^2")
root.geometry("1200x700")
root.configure(bg="#f5f5f5")

# ----------------- Header -----------------
header_frame = tk.Frame(root, bg="#f5f5f5")
header_frame.pack(side="top", fill="x", padx=20, pady=10)

logo_label = tk.Label(header_frame, text="News Broadcast", font=("Helvetica", 16, "bold"), bg="#f5f5f5", fg="#333333")
logo_label.pack(side="left")

nav_frame = tk.Frame(header_frame, bg="#f5f5f5")
nav_frame.pack(side="right")

nav_items = ["About", "Features", "Learn", "For Business", "Pricing", "Download"]
for item in nav_items:
    btn = tk.Button(nav_frame, text=item, font=("Arial", 10), bg="#f5f5f5", fg="#333333", bd=0,
                    activebackground="#e0e0e0", activeforeground="#000000",
                    command=lambda name=item: nav_click(name))
    btn.pack(side="left", padx=8)

try_btn = tk.Button(header_frame, text="Newz For All", font=("Arial", 10, "bold"), bg="#ffcc00", fg="#333333", bd=0, padx=10, pady=5)
try_btn.pack(side="right", padx=10)

# ----------------- Main Content -----------------
content_frame = tk.Frame(root, bg="#f5f5f5")
content_frame.pack(fill="both", expand=True, padx=20, pady=10)

# ---------------- Left Frame (Languages) ----------------
left_frame = tk.Frame(content_frame, width=150, bg="#f0f0f0")
left_frame.pack(side="left", fill="y", padx=10)

tk.Label(left_frame, text="Languages", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#333333").pack(pady=10)
languages = ["English", "Hindi", "Marathi", "Spanish", "French", "German"]
for lang in languages:
    tk.Button(left_frame, text=lang, font=("Arial", 12), bg="#ffcc00", fg="#333333", bd=0, padx=10, pady=5,
              command=lambda l=lang: on_language_click(l)).pack(pady=5, fill="x")

# ---------------- Center Frame (Headlines) ----------------
center_frame = tk.Frame(content_frame, bg="#f5f5f5")
center_frame.pack(side="left", fill="both", expand=True, padx=10)

title_label = tk.Label(center_frame, text="Get Current Updates. Read the news and stay updated.",
                       font=("Helvetica", 24, "bold"), bg="#f5f5f5", fg="#333333", wraplength=600, justify="center")
title_label.pack(pady=10)

subtitle_label = tk.Label(center_frame, text="Click further as per your preferences.", font=("Arial", 12),
                          bg="#f5f5f5", fg="#666666")
subtitle_label.pack(pady=5)

# Action Buttons
action_frame = tk.Frame(center_frame, bg="#f5f5f5")
action_frame.pack(pady=10)

start_btn = tk.Button(action_frame, text="Login", font=("Arial", 12, "bold"), bg="#ffcc00", fg="#333333", padx=15, pady=8, command=start_now)
start_btn.pack(side="left", padx=10)

learn_btn = tk.Button(action_frame, text="Stay logout", font=("Arial", 12), bg="#f5f5f5", fg="#333333", bd=0,
                      activebackground="#e0e0e0", activeforeground="#000000", command=learn_more)
learn_btn.pack(side="left", padx=10)

# Scrollable News Panel
prompt_frame = tk.Frame(center_frame, bg="#f5f5f5")
prompt_frame.pack(pady=10, fill="both", expand=True)

prompt_label = tk.Label(prompt_frame, text="HEADLINES", font=("Helvetica", 14, "bold"), bg="#f5f5f5", fg="#333333")
prompt_label.pack(anchor="w", padx=5)

prompt_list_frame = tk.Frame(prompt_frame, bg="#f5f5f5")
prompt_list_frame.pack(padx=5, pady=5, fill="both", expand=True)

canvas = tk.Canvas(prompt_list_frame, bg="#f5f5f5", highlightthickness=0)
scrollbar = tk.Scrollbar(prompt_list_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ---------------- Right Sidebar (Options) ----------------
right_frame = tk.Frame(content_frame, width=200, bg="#d9f0ff")
right_frame.pack(side="right", fill="y", padx=10)

tk.Label(right_frame, text="Options", font=("Helvetica", 10, "bold"), bg="#d9f0ff", fg="#333333").pack(pady=10)
sidebar_buttons = ["Business", "Crime", "Domestic", "Education", "Entertainment", "Environment", "Food", "Health", "Lifestyle", "Politics", "Science", "Sports", "Technology", "Top", "Tourism", "World", "Other"]

for btn_text in sidebar_buttons:
    tk.Button(right_frame, text=btn_text, font=("Arial", 10), bg="#ffcc00", fg="#333333", bd=0,
              padx=8, pady=3, command=lambda c=btn_text: on_category_click(c)).pack(pady=5, fill="x")

# ---------------- Info Label ----------------
info_label = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5f5", fg="#333333", wraplength=800, justify="center")
info_label.pack(pady=10)

# ---------------- Final GUI Update ----------------

refresh_headlines()
root.mainloop()
