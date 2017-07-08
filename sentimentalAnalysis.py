import tweepy
from textblob import TextBlob

consumer_key = '6GntQEwXYXcZ2sM6RUeHTJAJu'
consumer_secret = 'LBvN2vYyCp6TwgnAZSrYX7IdFEx2lS1eDsgvyh45FpMcYsvQH4'

access_token = '716518883516145664-MIXiB4GT69xIdJsTPmvMEAX94MevGig'
access_token_secret = 'o1uWzENprlC9sVzPhdF0RNGXJOBEmIWXNOZAGjNzMNGG0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Dubai')

for tweets in public_tweets:
	print(tweets.text)
	analysis = TextBlob(tweets.text)
	print(analysis.sentiment)