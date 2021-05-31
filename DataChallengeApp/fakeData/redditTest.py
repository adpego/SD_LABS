from lithops import storage, Storage
import json
from random import randint
import datetime


storageCloud = Storage()


for i in range(10):
    today = str(datetime.date.today()- datetime.timedelta(days=i))
    
    data = {
        'posts': []
    }

    for i in range(randint(200,300)):
        dataPost = {
            'title': "AAAAAAAAA",
            'text': "BBBBBBB",
            'sentiment': (randint(-1000,1000))/1000
        }
        data['posts'].append(dataPost)

    storageCloud.put_object('test-bythepego','test/reddit/'+today+'.json', json.dumps(data))
    
    