from lithops import storage, Storage
import json
from random import randint
import datetime


storageCloud = Storage()


for i in range(10):
    today = str(datetime.date.today()- datetime.timedelta(days=i))
    
    data = {
        'tweets': []
    }

    for i in range(randint(200,300)):
        dataTweet = {
            'id': (i+1)*randint(100,100000),
            'text': "AAAAAA",
            'sentiment': (randint(-1000,1000))/1000
        }
        data['tweets'].append(dataTweet)

    storageCloud.put_object('test-bythepego','test/twitter/'+today+'.json', json.dumps(data))
    
    