from lithops import Storage, storage
import json
import requests
import json
from datetime import date
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# storage = Storage()
# data = {
#     "patata": 1,
#     "Test": "nose",
# }
# storage.put_object('test-bythepego', 'data.json', json.dumps(data))
# data = storage.get_object('test-bythepego','redditTest1.json')

def getDataReddit(data):
    newDay = False
    today = str(date.today())
    
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    r = requests.get('https://www.reddit.com/r/Bitcoin/new/.json', headers=header)
    analyzer = SentimentIntensityAnalyzer() #sentiment

    if today not in data:
        data[today] = {
            'posts': []
        }
        newDay = True

    for post in r.json()['data']['children']:
        if post['data']['selftext']:
            dataPost = {
                'title': post['data']['title'],
                'text': post['data']['selftext'],
                'sentiment': analyzer.polarity_scores(post['data']['selftext'])['compound']
            }
            data[today]['posts'].append(dataPost)

    return data, newDay




storageCloud = Storage()

try:
    data = storageCloud.get_object('test-bythepego', 'reddit.json')
    data = json.loads(data)
except storage.utils.StorageNoSuchKeyError:
    data = {}



dataReddit, newDay = getDataReddit(data)
if newDay:
    data.update(dataReddit)

else:
    data = dataReddit
 

storageCloud.put_object('test-bythepego','reddit.json', json.dumps(data))

# data = json.loads(data)

# dataBitcoin, newDay = getDataBitcoin(data)

# if newDay:
#     data.update(dataBitcoin)
# else:
#     data = dataBitcoin
   
# storage.put_object('test-bythepego','bitcoin.json', json.dumps(data))
# print(data)
