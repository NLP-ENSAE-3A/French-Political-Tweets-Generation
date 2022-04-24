import pandas as pd
from tqdm import tqdm_notebook

import tweepy

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '823147464656031744-PfBPMbuwlM1XGni4NudViUjKjn1gJr7'
ACCESS_SECRET = '4buGjzlIPQeHbpZt1vzuYidIMr7fvGsFcqhpYfOYZHqz7'
CONSUMER_KEY = 'YvGl3Q4IZVL0sC6hnaDKDdete'
CONSUMER_SECRET = '95MU1b6KpuvPX856qC7Y8UTYoCn9itusgCr2HllHYz0lpr7aRo'
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGVSaAEAAAAAWThCSC%2BRmpY8paAGsu5fav%2FzqxE%3DVlhxBhzyQnoncRIfQLOUFBPrmwaiNKoeqPczYG97Me0GxwS9BB"


# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api


# Create API object
api = connect_to_twitter_OAuth()

influencers_id_list = [
    1417065346259947521,
    1027237988248506369,
    1484804599596863488,
    1472880947863465990,
    1500861845325946884,
    3349246193,
    1460623997931069440,
    1400701733781884929,
    1474776004027686923,
    1485905005680988161,
    2470686049,
    304545927,
    1425908448,
    269809161,
    1331280300345860098,
    1489881563600936960,
    1300273674,
    489349253,
    1370482997590392834,
    1472180687373484033,
    1183418538285027329    
    
]

def scrap_tweets(influencers_id_list,ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET,BEARER_TOKEN,filename):
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    client = tweepy.Client(bearer_token=BEARER_TOKEN,
                    consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token=ACCESS_TOKEN,
                    access_token_secret=ACCESS_SECRET)
    
    
    tweets = []
    
    print('\n***** Extracting Tweets *****\n')
    for id_ in tqdm_notebook(influencers_id_list):

        tweepy_request = client.get_users_tweets(id=str(id_), max_results=100)
        if tweepy_request.data != None:
            tweets.extend([tweet.text for tweet in tweepy_request.data])
            oldest_id = tweepy_request.meta['oldest_id']

            try:
                while True: 
                    tweepy_request = client.get_users_tweets(id=str(id_),
                                                                        max_results=100, 
                                                                        until_id=oldest_id,
                                                                        exclude='retweets')
                    new_tweets = [tweet.text for tweet in tweepy_request.data]
                    oldest_id = tweepy_request.meta['oldest_id']
                    tweets.extend(new_tweets)
            except TypeError:
                print(f'Tweets from id {id_} extracted !')
        else:
            print(f'No tweets retrieved from {id_} !')

    print('\n***** Saving Tweets *****\n')
    
    df = pd.DataFrame(None,columns=['tweet'])
    
    for tweet in tqdm_notebook(tweets):
        df = df.append({'tweet':tweet},ignore_index=True)
        
    
    df.to_csv(f'{filename}.csv')



if __name__ == "__main__":
  
	scrap_tweets(
	influencers_id_list=influencers_id_list,
	ACCESS_TOKEN=ACCESS_TOKEN,
	ACCESS_SECRET=ACCESS_SECRET,
	CONSUMER_KEY=CONSUMER_KEY,
	CONSUMER_SECRET=CONSUMER_SECRET,
	BEARER_TOKEN=BEARER_TOKEN,
	filename='tweets_extract')