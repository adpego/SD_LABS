import requests
import json
from datetime import date
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from lithops import Storage, storage

def getDataReddit(data):
    
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    r = requests.get('https://www.reddit.com/r/Bitcoin/new/.json', headers=header)
    analyzer = SentimentIntensityAnalyzer() #sentiment

    for post in r.json()['data']['children']:
        if post['data']['selftext']:
            dataPost = {
                'title': post['data']['title'],
                'text': post['data']['selftext'],
                'sentiment': analyzer.polarity_scores(post['data']['selftext'])['compound']
            }
            data['posts'].append(dataPost)
    return data

def main():
    storageCloud = Storage()
    today = str(date.today())
    try:
        data = storageCloud.get_object('test-bythepego', 'reddit/'+today+'.json')
        data = json.loads(data)
    except storage.utils.StorageNoSuchKeyError:
        data = {
            'posts': []
        }
        
    data = getDataReddit(data)

    storageCloud.put_object('test-bythepego','reddit/'+today+'.json', json.dumps(data))

if __name__ == "__main__":
    main()