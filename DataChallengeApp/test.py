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
        "NumPostsPositive": 0,
        "NumPostsNegative": 0,
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
                dataPosts['NumPostsPositive'] += 1
            else: # sentiment negative
                dataPosts['NumPostsNegative'] += 1

        else:  # without sentiment
            dataPosts['NumPostNoSent'] += 1
        dataPosts['NumPosts'] += 1

    if dataPosts['NumPostSent'] != 0:
        dataPosts['SentimentAvg'] /= dataPosts['NumPostSent']


    return dataPosts

def getDataTwitter(date):

    dataPosts = {
        "NumPosts": 0,
        "NumPostSent": 0,
        "NumPostNoSent": 0,
        "NumPostsPositive": 0,
        "NumPostsNegative": 0,
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
                dataPosts['NumPostsPositive'] += 1
            else: # sentiment negative
                dataPosts['NumPostsNegative'] += 1

        else:  # without sentiment
            dataPosts['NumPostNoSent'] += 1
        dataPosts['NumPosts'] += 1

    if dataPosts['NumPostSent'] != 0:
        dataPosts['SentimentAvg'] /= dataPosts['NumPostSent']

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
    for i in range(10,-1,-1):
        today = str(datetime.date.today()-datetime.timedelta(days=i))
        days.append(today)


    with Pool() as pool:
        resultRedditAsync = pool.map_async(getDataReddit, days)
        resultTwitterAsync = pool.map_async(getDataTwitter, days)
        resultBitcoinAsync = pool.map_async(getDataBitcoin, days)
        
    return resultRedditAsync.get(), resultTwitterAsync.get(), resultBitcoinAsync.get(), days

dataReddit, dataTwitter, dataBitcoin, days = getData(1,3)
dataReddit, dataTwitter, dataBitcoin, days = getData(1,3)
dataRedditSentiment = [post['SentimentAvg'] for post in dataReddit]
dataTwitterSentiment = [post['SentimentAvg'] for post in dataTwitter]


fig, axs = plt.subplots(2)
fig.tight_layout(pad=2.0)
day = days
#day = [0.5,0.2,0.3,-0.1,-0.4,0.3,0.7]
#dataRedditSentiment = [0.5,0.2,0.3,-0.1,-0.4,0.3,0.7]
#dataTwitterSentiment = [0.4,0.3,0.4,-0.2,-0.5,0.1,0.5]
lineReddit = axs[0].plot(day, dataRedditSentiment, color='#FF4500')
lineTwitter = axs[0].plot(day, dataTwitterSentiment, color='#1da1f2')
#axs[0].set_xlabel('Day',color="green")
axs[0].set_ylabel('Sentiment',color="green")
axs[0].set_title('Sentiment Reddit/Twitter')
axs[0].legend(['Reddit', 'Twitter'], loc=3)
axs[0].axhline(y=0, color='black', linestyle='-')
axs[0].grid(True)

#plt.show()


#dataBitcoin = [4,3,2,12,3,54,3]
lineReddit = axs[1].plot(day, dataBitcoin, color='#f2a900')
axs[1].set_xlabel('Day',color="green")
axs[1].set_ylabel('Sentiment',color="green")
axs[1].set_title('Bitcoin')
axs[1].legend(['Reddit'], loc=3)
axs[1].axhline(y=20000, color='black', linestyle='-')
axs[1].grid(True)


plt.setp(axs[0].get_xticklabels(), rotation=30, horizontalalignment='right')
plt.setp(axs[1].get_xticklabels(), rotation=30, horizontalalignment='right')

plt.show()



totalPositivePostsTwitter = sum([post['NumPostsPositive'] for post in dataTwitter])
totalNegativePostsTwitter = sum([post['NumPostsNegative'] for post in dataTwitter])
totalNoSentPostsTwitter = sum([post['NumPostNoSent'] for post in dataTwitter])

totalPositivePostsReddit = sum([post['NumPostsPositive'] for post in dataReddit])
totalNegativePostsReddit = sum([post['NumPostsNegative'] for post in dataReddit])
totalNoSentPostsReddit = sum([post['NumPostNoSent'] for post in dataReddit])

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(10,10))
# Pie chart
labels = ['Negative', 'Non-Sentiment', 'Positive']
colors = ['#ff9999','#9a9a9a','#99ff99']
explode = (0.05,0.05,0.05)

sizesTwitter = [totalNegativePostsTwitter, totalNoSentPostsTwitter, totalPositivePostsTwitter]# only "explode" the 2nd slice (i.e. 'Hogs')
#explode = (0, 0.1, 0, 0)#add colors
#fig1, ax1 = plt.subplots()
ax1.pie(sizesTwitter, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, explode = explode)# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
ax1.set_title("TWITTER")

sizesReddit = [totalNegativePostsReddit, totalNoSentPostsReddit, totalPositivePostsReddit]
ax2.pie(sizesReddit, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, explode = explode)# Equal aspect ratio ensures that pie is drawn as a circle
ax2.axis('equal')
ax2.set_title("REDDIT")
fig.suptitle("2021-05-22 to 2021-05-27", fontsize=14)
plt.tight_layout()
plt.show()

