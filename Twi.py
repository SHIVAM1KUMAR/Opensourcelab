import tweepy
consumer_key = "XXXX" #Your API/Consumer key 
consumer_secret = "XXXX" #Your API/Consumer Secret Key
access_token = "XXXX" #Your Access token key
access_token_secret = "XXXX" #Your Access token Secret key
auth = tweepy.OAuth1UserHandler(
 consumer_key, consumer_secret,
 access_token, access_token_secret
)
api = tweepy.API(auth, wait_on_rate_limit=True)
username = "john"
no_of_tweets =100
try:
 tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
 attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source, tweet.text] for tweet in 
tweets]
 columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
 tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
 print('Status Failed On,',str(e))
 time.sleep(3)