import requests
from datetime import date, time
from lithops import Storage, storage
import json

def getDataBitcoin(data):
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    bitcoinData = r.json()

    data['priceArray'].append(bitcoinData['bpi']['EUR']['rate_float'])
    return data

def main():
    storageCloud = Storage()
    today = str(date.today())
    try:
        data = storageCloud.get_object('test-bythepego', 'bitcoin/'+today+'.json')
        data = json.loads(data)
    except storage.utils.StorageNoSuchKeyError:
        data = {
            'priceArray': []
        }

    data = getDataBitcoin(data)
    
    storageCloud.put_object('test-bythepego','bitcoin/'+today+'.json', json.dumps(data))

if __name__ == "__main__":
    main()