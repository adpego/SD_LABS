import requests
import time
from lithops.multiprocessing import Pool

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

ERROR = 46

def getComments(comments, data):
    
    for comment in comments['data']['children']:

        #if 'body' in comment['data']:
        data.append(comment['data']['body'])

        if ('replies' in comment['data']) and (comment['data']['replies'] != ''):
            getComments(comment['data']['replies'], data)
    
    

def readComments(url):
    r = requests.get("https://www.reddit.com/r/Bitcoin/comments/nkhrnj/daily_discussion_may_25_2021/.json", headers=header)
    hasReplies = True
    data = []
    
    
    getComments(r.json()[1], data)
    data_set = set(data)
    print(len(data_set) == len(data))
    print(len(data))
        
            


def getUrls():
    r = requests.get("https://www.reddit.com/r/Bitcoin/top/.json", headers=header)
    urls = []
    for post in r.json()['data']['children']:
        if(post['data']['num_comments'] > 20):
            urls.append([post['data']['url'],post['data']['num_comments']])

    
    for i in range(5):
        moreComments = 0

        if len(urls) == 0: 
            break
        
        for url in urls:
            if url[1] > moreComments:
                urlImportant = url
                moreComments = url[1]
        urls.remove(urlImportant)
        
        

#getUrls()

#readComments("https://www.reddit.com/r/Bitcoin/comments/nkhrnj/daily_discussion_may_25_2021/.json")

def test(num):
    return {'test': time.time()}
with Pool() as pool:
    print(pool.map(test, [3]))
    print(time.time())
    