print("Note : Now this can't work because api key not inserted")

import requests
import json

if __name__ == '__main__':
    url = "Enter_your_api_key_Here"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])

# ---------------------------Note-----------------------------------------
print("\nFor learn how to run and access print_daily_news , open this file in your editor and learn about this file")
print("\nThank You\n")