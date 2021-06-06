import json
import tweepy
from datetime import date, datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from lithops import Storage, storage

def getDataTwitter(data):
    with open('twitter_credentials.json', 'r') as file:
        creds = json.load(file)

    auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

    analyzer = SentimentIntensityAnalyzer() #sentiment

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
   
    new_search = 'bitcoin'
    today = date.today()
    start_date = datetime(today.year, today.month, today.day, 00, 00, 00)
    end_date = datetime(today.year, today.month, today.day, 23, 59, 59)

    for tweet in tweepy.Cursor(api.search,
                    q=new_search,
                    lang='en',
                    result_type='recent',
                    tweet_mode='extended'
                    ).items(300): 
        if tweet.created_at < end_date and tweet.created_at > start_date:
            dataTweet = {
                'id': tweet.id,
                'text': tweet.full_text,
                'sentiment': analyzer.polarity_scores(tweet.full_text)['compound']
            }
            data['tweets'].append(dataTweet)
    
    return data

def main():
    storageCloud = Storage()
    today = str(date.today())
    try:
        data = storageCloud.get_object('test-bythepego', 'twitter/'+today+'.json')
        data = json.loads(data)
    except storage.utils.StorageNoSuchKeyError:
        data = {
            'tweets': []
        }

    data = getDataTwitter(data)
    storageCloud.put_object('test-bythepego','twitter/'+today+'.json', json.dumps(data))

if __name__ == "__main__":
    main()