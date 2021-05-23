from lithops import Storage
import datetime
from lithops.multiprocessing import Pool
import json
'''storage = Storage()
data = storage.list_objects('test-bythepego', prefix='twitter/')

for files in data:
    aux = files['Key'].split('/')
    print(aux[len(aux)-1].split('.')[0])'''

'''def getDataReddit(date):
    storage = Storage()
    data = json.loads(storage.get_object('test-bythepego', 'test/reddit/'+date+'.json'))
    sentimentAvg = 0
    for post in data['posts']:
        sentimentAvg += post['sentiment']
    sentimentAvg /= len(data['posts'])
    return sentimentAvg

days = []
for i in range(1,8):
    today = str(datetime.date.today()-datetime.timedelta(days=i))
    days.append(today)

with Pool() as pool:
    result = pool.map(getDataReddit, days)
    print(result)'''

def double(i):
    storage = Storage()
    return i * 2

with Pool() as pool:
    result = pool.map(double, [1, 2, 3, 4, 5])
    print(result)

'''
import json    
data = json.loads(storage.get_object('test-bythepego', 'test/twitter/2021-05-22.json'))
sentimentAvg = 0
for tweet in data['tweets']:
    sentimentAvg += tweet['sentiment']
sentimentAvg /= len(data['tweets'])
print(sentimentAvg)




data = json.loads(storage.get_object('test-bythepego', 'bitcoin/2021-05-19.json'))
print(len(data['priceArray']))'''