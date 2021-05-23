from lithops import storage, Storage
import json
from random import randint
import datetime


# storageCloud = Storage()
# today = '2021-05-20'
# try:
#     data = storageCloud.get_object('test-bythepego', 'bitcoin/'+today+'.json')
#     data = json.loads(data)
# except storage.utils.StorageNoSuchKeyError:
#     data = {
#         'priceArray': []
#     }

# print(len(data['priceArray']))

storageCloud = Storage()
data = {
    'posts': []
}

for i in range(10):
    today = str(datetime.date.today()- datetime.timedelta(days=i))
    
    data = {
        'priceArray': []
    }

    for _ in range(96):
        data['priceArray'].append(randint(2000000,6000000)/100)
    print(data)
    storageCloud.put_object('test-bythepego','test/bitcoin/'+today+'.json', json.dumps(data))