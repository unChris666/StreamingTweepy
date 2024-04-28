# Streaming tweets from home timeline

public_tweet = api.home_timeline(count=5)

for tweet in public_tweet:
    print("-->",tweet.text)