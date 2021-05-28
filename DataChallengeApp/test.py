import matplotlib.pyplot as plt
import datetime
from lithops import Storage, storage
from lithops.multiprocessing import Pool
import json

def getDataReddit(date):

    dataPosts = {
        "NumPosts": 0,
        "NumPostSent": 0,
        "NumPostNoSent": 0,
        "PercentPostsPositive": 0,
        "PercentPostsNegative": 0,
        "SentimentAvg": 0,
    }

    storageCloud = Storage()
    try:
        data = json.loads(storageCloud.get_object('test-bythepego', 'reddit/'+date+'.json'))
    except storage.utils.StorageNoSuchKeyError:
        return dataPosts

    for post in data['posts']:
        if post['sentiment'] != 0: # with sentiment
            dataPosts['SentimentAvg'] += post['sentiment']
            dataPosts['NumPostSent'] += 1

            if post['sentiment'] > 0: # sentiment positive
                dataPosts['PercentPostsPositive'] += 1
            else: # sentiment negative
                dataPosts['PercentPostsNegative'] += 1

        else:  # without sentiment
            dataPosts['NumPostNoSent'] += 1
        dataPosts['NumPosts'] += 1

    if dataPosts['NumPostSent'] != 0:
        dataPosts['SentimentAvg'] /= dataPosts['NumPostSent']
        dataPosts['PercentPostsPositive'] /= dataPosts['NumPostSent']
        dataPosts['PercentPostsNegative'] /= dataPosts['NumPostSent']

    return dataPosts

def getDataTwitter(date):

    dataPosts = {
        "NumPosts": 0,
        "NumPostSent": 0,
        "NumPostNoSent": 0,
        "PercentPostsPositive": 0,
        "PercentPostsNegative": 0,
        "SentimentAvg": 0,
    }

    storageCloud = Storage()
    try:
        data = json.loads(storageCloud.get_object('test-bythepego', 'twitter/'+date+'.json'))
    except storage.utils.StorageNoSuchKeyError:
        return dataPosts

    for post in data['tweets']:
        if post['sentiment'] != 0: # with sentiment
            dataPosts['SentimentAvg'] += post['sentiment']
            dataPosts['NumPostSent'] += 1

            if post['sentiment'] > 0: # sentiment positive
                dataPosts['PercentPostsPositive'] += 1
            else: # sentiment negative
                dataPosts['PercentPostsNegative'] += 1

        else:  # without sentiment
            dataPosts['NumPostNoSent'] += 1
        dataPosts['NumPosts'] += 1

    if dataPosts['NumPostSent'] != 0:
        dataPosts['SentimentAvg'] /= dataPosts['NumPostSent']
        dataPosts['PercentPostsPositive'] /= dataPosts['NumPostSent']
        dataPosts['PercentPostsNegative'] /= dataPosts['NumPostSent']

    return dataPosts

def getDataBitcoin(date):
    storageCloud = Storage()
    try:
        data = json.loads(storageCloud.get_object('test-bythepego', 'bitcoin/'+date+'.json'))
    except storage.utils.StorageNoSuchKeyError:
        return 0
    
    priceAvg = 0
    for price in data['priceArray']:
        priceAvg += price
    
    if priceAvg != 0:
        priceAvg /= len(data['priceArray'])

    return priceAvg

def getData(dateIni, days):
    days = []
    for i in range(2,-1,-1):
        today = str(datetime.date.today()-datetime.timedelta(days=i))
        days.append(today)


    with Pool() as pool:
        resultRedditAsync = pool.map_async(getDataReddit, days)
        resultTwitterAsync = pool.map_async(getDataTwitter, days)
        resultBitcoinAsync = pool.map_async(getDataBitcoin, days)
        
    return resultRedditAsync.get(), resultTwitterAsync.get(), resultBitcoinAsync.get(), days


dataReddit, dataTwitter, dataBitcoin, days = getData(1,3)
dataRedditSentiment = [post['NumPosts'] for post in dataReddit]
dataTwitterSentiment = [post['NumPosts'] for post in dataTwitter]



day = days
#dataReddit = [0.5,0.2,0.3,-0.1,-0.4,0.3,0.7]
#dataTwitter = [0.4,0.3,0.4,-0.2,-0.5,0.1,0.5]
lineReddit = plt.plot(day, dataRedditSentiment, color='#FF4500')
lineTwitter = plt.plot(day, dataTwitterSentiment, color='#1da1f2')
plt.xlabel('Day',color="green")
plt.ylabel('Sentiment',color="green")
plt.title('Sentiment Reddit/Twitter')
plt.legend(['Reddit', 'Twitter'], loc=3)
plt.axhline(y=0, color='black', linestyle='-')
plt.grid(True)
plt.show()



lineReddit = plt.plot(day, dataBitcoin, color='#FF4500')
plt.xlabel('Day',color="green")
plt.ylabel('Sentiment',color="green")
plt.title('Sentiment Reddit/Twitter')
plt.legend(['Reddit'], loc=3)
plt.axhline(y=20000, color='black', linestyle='-')
plt.grid(True)
plt.show()

