import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
news_api_key = "YOUR OWN API KEY" 
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
api_key = "YOUR OWN API KEY" 

news_params = {'apiKey':news_api_key,
 'q':COMPANY_NAME
}
stock_params = {
'function':'TIME_SERIES_DAILY',
'symbol':STOCK_NAME,
'apikey':api_key
}
response = requests.get(url=STOCK_ENDPOINT,params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]

yesterday_closing_data = yesterday_data['4. close']
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_data = day_before_yesterday_data['4. close']
difference = abs(float(day_before_yesterday_closing_data)-float(yesterday_closing_data))
diff_percent = (difference/float(yesterday_closing_data))*100


if diff_percent>3:
    response = requests.get(url=NEWS_ENDPOINT,params = news_params)
    articles = response.json()['articles']
    top3_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}.\nBrief:{article['description']} "for article in top3_articles]
    for article in formatted_articles:
        print(article)
