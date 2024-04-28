# Twitter API authentication

import tweepy

api_key =  "EgBvdsTMjH5Xs65dg0vQUueTx"
api_secret_key = "QUJ4HXShLkjYHTkQtNykrjAsAV2VxpVtnWDhz0GTvKWcBRiBGy"
access_token =  "1576500399929819136-8T1pNyEcpxMLJZJHHERvueBs7ZIwGw"
access_token_secret =  "HsEsFdaLrBoNcU2PxzIgSTw1NAKPAWbvlEWLWTRINwngW"

# authorize the API Key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the api
api = tweepy.API(authentication)