import requests

api_key = "85ad2a63990d4ee6a4e65ba33fc95a9b"

# First try top headlines in India
url_headlines = "https://newsapi.org/v2/top-headlines"
params_headlines = {"country": "in", "apiKey": api_key}
response = requests.get(url_headlines, params=params_headlines)
data = response.json()

if data["status"] == "ok" and data.get("articles"):
    articles = data["articles"]
else:
    # Fallback to keyword search
    url_everything = "https://newsapi.org/v2/everything"
    params_everything = {"q": "technology", "sortBy": "publishedAt", "apiKey": api_key}
    response = requests.get(url_everything, params=params_everything)
    data = response.json()
    articles = data.get("articles", [])

# Print top 5 articles
if articles:
    for i, article in enumerate(articles[:5], start=1):
        print(f"\n{i}. {article['title']}")
        print(article['url'])
else:
    print("⚠️ No articles found.")
