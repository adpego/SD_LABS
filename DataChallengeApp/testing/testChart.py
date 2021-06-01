# plot_time_series.py

import matplotlib.pyplot as plt

from datetime import datetime, timedelta, date
import random
import numpy as np
import pandas as pd 


def getDays(dateIni, dateFin):

    days = []
    
    if dateIni > dateFin:
        dateIni, dateFin = dateFin, dateIni

    if dateFin > date.today():
        dateFin = date.today()
    
    cont = 1
    while dateIni != dateFin:
        days.append(dateIni)
        dateIni += timedelta(days=1)
        
    days.append(dateIni)
    return days

aux = [str(day) for day in getDays(date(2021, 5, 23), date.today())]

print(aux)

print(date.today())
"""


datas = []


dataPosts = {
        "NumPosts": 0,
        "NumPostSent": 0,
        "NumPostNoSent": 0,
        "NumPostsPositive": 0,
        "NumPostsNegative": 0,
        "SentimentAvg": 0,
        "SetimentCount": {}
    }

    # Inicialize sentiment count

for i in range(-10,11):
    if i == 0:
        dataPosts["SetimentCount"]["-"+str(i)] = 0

    dataPosts["SetimentCount"][str(i)] = 0

print(dataPosts)


def getCountAverageSentiment(data):

    datasCounts = [dataCount['SetimentCount'] for dataCount in data]
    totalNumPostsSentiment = sum([dataCount['NumPostSent'] for dataCount in data])
    datasCountsAvg = {}

    for dataCount in datasCounts:
        for key in dataCount:
            if key in datasCountsAvg:
                datasCountsAvg[key] += dataCount[key]
            else:
                datasCountsAvg[key] = dataCount[key]

    for key in datasCountsAvg:
        datasCountsAvg[key] /= len(data)

    return [datasCountsAvg[key]/totalNumPostsSentiment*1000 for key in datasCountsAvg]

data1 = {'NumPosts': 0, 'NumPostSent': 0, 'NumPostNoSent': 0, 'NumPostsPositive': 0, 'NumPostsNegative': 0, 'SentimentAvg': 0, 'SetimentCount': {'-10': 3, '-9': 0, '-8': 0, '-7': 0, '-6': 0, '-5': 0, '-4': 0, '-3': 0, '-2': 0, '-1': 2, '1': 0, '2': 0, '3': 5, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 5}}
data2 = {'NumPosts': 0, 'NumPostSent': 0, 'NumPostNoSent': 0, 'NumPostsPositive': 0, 'NumPostsNegative': 0, 'SentimentAvg': 0, 'SetimentCount': {'-10': 1, '-9': 0, '-8': 0, '-7': 0, '-6': 0, '-5': 0, '-4': 0, '-3': 0, '-2': 0, '-1': 2, '1': 0, '2': 0, '3': 3, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 3}}
datas.append(data1)
datas.append(data2)




print(getCountAverageSentiment(datas))
print(datetime.datetime.today())
#create dataframe
df = pd.DataFrame({'Sent': ['-10', '(-10, -9]','(-9, -8]','(-8, -7]','(-7, -6]','(-6, -5]','(-5, -4]','(-4, -3]','(-3, -2]','(-2, -1]','(-1, 0]','(0, 1)','[1, 2)','[2, 3)','[3, 4)','[4, 5)','[5, 6)', '[6, 7)', '[7, 8)','[8, 9)','[9, 10)','10'], 
                    'Reddit': [9000, 14000, 22000, 26000, 34000, 32000, 29000, 22000, 14000, 3000, 9000, 14000, 22000, 26000, 34000, 32000, 29000, 22000, 14000, 3000, 5000, 7000], 
                    'Twitter': [8000, 15000, 19000, 28000, 35000, 34000, 28000, 24000, 17000, 5000, 9000, 14000, 22000, 26000, 34000, 32000, 29000, 22000, 14000, 3000, 5000, 7000]})



#define x and y limits
y = range(0, len(df))
x_reddit = df['Reddit']
x_twitter = df['Twitter']

#define plot parameters
fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(9, 6))

#specify background color and plot title
fig.patch.set_facecolor('xkcd:light grey')
plt.figtext(.5,.91,"# comment with specific sentiment \n(every 1000 posts)\n 2021-05-23 to 2021-05-29", fontsize=15, ha='center')
    
#define male and female bars
axes[0].barh(y, x_reddit, align='center', color='#FF4500')
axes[0].set(title='Reddit')
axes[1].barh(y, x_twitter, align='center', color='#1da1f2')
axes[1].set(title='Twitter')

#adjust grid parameters and specify labels for y-axis
axes[1].grid()
axes[0].set(yticks=y, yticklabels=df['Sent'])
axes[0].invert_xaxis()
axes[0].grid()

#display plot
plt.show()          



exit()
plt.style.use('seaborn')

dates = []
print(4*24)
date = datetime(2021, 5, 10, 0, 0, 0)
for i in range(365):
    for time in range(96):
        dates.append(date)
        date = date+timedelta(minutes=15)


y = []
num = random.randint(30000,40000)
for i in range(96*365):
    if random.randint(0,1):
        num += 20
    else:
        num -= 20
    y.append(num)


#y = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]


#plt.tight_layout()
#plt.grid(True)
#plt.show()



lineReddit = plt.plot(dates, y, color='#FF4500')
plt.xlabel('Day',color="green")
plt.ylabel('Sentiment',color="green")
plt.title('Sentiment Reddit/Twitter')
plt.legend(['Reddit'], loc=3)
plt.axhline(y=20000, color='black', linestyle='-')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
"""