# Streaming tweets from user timeline

user = "AnalyticsVidhya"
public_tweet = api.user_timeline(id=user,count=5)

for tweet in public_tweet:
    print("-->",tweet.text)