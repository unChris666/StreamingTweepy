# Retrieve tweets
result = api.search(['covid','Covid-19','COVID-19'], lang='en', count=10)

# JSON keys
pprint(result[0]._json.keys())