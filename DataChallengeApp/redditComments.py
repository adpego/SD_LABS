import requests
import time
from lithops import Storage, storage
from datetime import date
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

analyzer = SentimentIntensityAnalyzer() #sentiment

def getComments(comments, data):
    
    for comment in comments['data']['children']:

        if 'body' in comment['data']:
            dataPost = {
                'text': comment['data']['body'],
                'sentiment': analyzer.polarity_scores(comment['data']['body'])['compound']
            }
            data['posts'].append(dataPost)
    
        if ('replies' in comment['data']) and (comment['data']['replies'] != ''):
            getComments(comment['data']['replies'], data)
    
    
def readComments(url, data):
    r = requests.get(url, headers=header)
    if len(r.text) == 46:
        return data
    try:    
        getComments(r.json()[1], data)
    except:
        pass
    
    return data
            


def getUrls():
    r = requests.get("https://www.reddit.com/r/Bitcoin/top/.json", headers=header)
    if len(r.text) == 46:
        return []
    urls = []
    for post in r.json()['data']['children']:
        if(post['data']['num_comments'] > 50):
            urls.append(["https://www.reddit.com"+post['data']['permalink']+".json",post['data']['num_comments']])

    urlsImportant = []
    for i in range(len(urls)):
        moreComments = 0    
        for url in urls:
            if url[1] > moreComments:
                urlImportant = url
                moreComments = url[1]
        urls.remove(urlImportant)
        urlsImportant.append(urlImportant)

    return urlsImportant
        
        


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
    urls = getUrls()
    for url in urls:
        data = readComments(url[0], data)
        time.sleep(5)

    storageCloud.put_object('test-bythepego','reddit/'+today+'.json', json.dumps(data))

if __name__ == "__main__":
    main()