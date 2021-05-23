from lithops import storage, Storage
import json
from random import randint
import datetime


storageCloud = Storage()
# today = '2021-05-20'
# try:
#     data = storageCloud.get_object('test-bythepego', 'bitcoin/'+today+'.json')
#     data = json.loads(data)
# except storage.utils.StorageNoSuchKeyError:
#     data = {
#         'priceArray': []
#     }

# print(len(data['priceArray']))

#storageCloud = Storage()



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
    
    

# for _ in range(96):
#     data['priceArray'].append(randint(2000000,6000000)/100)
#     print(data)
#     storageCloud.put_object('test-bythepego','test/bitcoin/'+today+'.json', json.dumps(data))