from lithops import Storage, storage
import datetime
from lithops.multiprocessing import Pool
import json
'''storage = Storage()
data = storage.list_objects('test-bythepego', prefix='twitter/')

for files in data:
    aux = files['Key'].split('/')
    print(aux[len(aux)-1].split('.')[0])'''

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
    for i in range(0,7):
        today = str(datetime.date.today()-datetime.timedelta(days=i))
        days.append(today)


    with Pool() as pool:
        resultTwitterAsync = pool.map_async(getDataTwitter, days)
        resultRedditAsync = pool.map_async(getDataReddit, days)
        resultBitcoinAsync = pool.map_async(getDataBitcoin, days)
        
    return resultTwitterAsync.get(), resultRedditAsync.get(), resultBitcoinAsync.get()

