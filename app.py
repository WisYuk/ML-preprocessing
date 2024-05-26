import tweepy
import pandas as pd

# Twitter API credentials
consumer_key = "" # Your API/Consumer key 
consumer_secret = "" # Your API/Consumer Secret Key
access_token = ""    # Your Access token key
access_token_secret = "" # Your Access token Secret key

# Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

# Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "sex for grades"
no_of_tweets = 10

try:
    # The number of tweets we want to retrieve from the search
    tweets = api.search_tweets(q=search_query, count=no_of_tweets)
    
    # Pulling some attributes from the tweet
    attributes_container = [
        [tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.text]
        for tweet in tweets
    ]

    # Creation of column list to rename the columns in the DataFrame
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    # Creation of DataFrame
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
    
    # Outputting data to CSV file
    tweets_df.to_csv('tweets.csv', index=False)
    print("Tweets have been successfully saved to tweets.csv")

except BaseException as e:
    print('Status Failed On,', str(e))
