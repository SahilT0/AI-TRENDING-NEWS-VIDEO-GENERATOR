import requests
import random

def get_title_and_content_from_same_article():
    NEWS_API_KEY = "e606032086fe4e479b992f987df06a28"
    url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=10&apiKey={NEWS_API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        articles = data.get("articles", [])
        if not articles:
            print("No articles found.")
            return None, None

        article = random.choice(articles)

        title = article.get("title", "") or "No Title"
        content = article.get("description", "") or article.get("content", "") or "No Content"

        return title.strip(), content.strip()

    except Exception as e:
        print("Error fetching news:", e)
        return None, None

