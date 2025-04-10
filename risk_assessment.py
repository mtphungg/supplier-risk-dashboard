import requests

API_KEY = '85bf6d35e5d4478f88122ed5885c5869'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

def get_news_risk(country):
    response = requests.get(NEWS_API_URL, params={
        'country': country,
        'apiKey': API_KEY
    })
    if response.status_code != 200:
        return 0  
    
    data = response.json()
    
    risk_score = 0
    for article in data['articles']:
        title = article['title'].lower()
        if any(keyword in title for keyword in ['strike', 'war', 'protest', 'delay', 'accident']):
            risk_score += 1

    return risk_score

if __name__ == '__main__':
    country = 'us'  
    print(f"Risk score for {country}: {get_news_risk(country)}")

