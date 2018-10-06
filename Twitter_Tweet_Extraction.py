try:
    import json
except ImportError:
    import simplejson as json

import csv

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

number_of_tweet = 100
filename = 'tweets.csv'
query = '#MUFC  -filter:retweets'
total_num_of_tweets = 0

ACCESS_TOKEN = '1040311982015037440-1TSqPfFZmXn1fUS1qplchjVbWBMANn'
ACCESS_SECRET = 'K0efO3na1D9Mw1Du7rkROzgOW8zDTLTG6AcVTuLqMzjQq'
CONSUMER_KEY = 'j4kLoamWfoPbw72VLoQwjmzeF'
CONSUMER_SECRET = 'UwEGlKxK2xX4I59FXhwUmc1A4wPoW2ZceTY1ZI2iTdEGDOaOjY'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)

search_results = twitter.search.tweets(q=query, lang='en', count=number_of_tweet)
json_str = json.dumps(search_results, indent=4)
result = json.loads(json_str)

#print(len(result['statuses']))
id_positon = len(result['statuses'])-1
id_for_next_time=result['statuses'][id_positon]['id']
total_num_of_tweets += (id_positon+1)

print("Loading...", end='')

with open (filename, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['id', 'user', 'created_at', 'text'])
    for x in range(0,id_positon):
        writer.writerow([result['statuses'][x]['id'],result['statuses'][x]['user']['name'],result['statuses'][x]['created_at'],result['statuses'][x]['text']])
                                           
for z in range(12):
    search_results = twitter.search.tweets(q=query, lang='en', count=number_of_tweet, max_id =id_for_next_time)
    json_str = json.dumps(search_results, indent=4)
    result = json.loads(json_str)

    #print(len(result['statuses']))
    id_positon = len(result['statuses'])-1
    total_num_of_tweets += (id_positon+1)
    if id_positon == -1:
        break
    id_for_next_time=result['statuses'][id_positon]['id']
    
    
    print("...", end='')
    
    with open (filename, 'a', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        for x in range(1,id_positon):
            writer.writerow([result['statuses'][x]['id'],result['statuses'][x]['user']['name'],result['statuses'][x]['created_at'],result['statuses'][x]['text']])

print("Done! Total Tweets: %d",total_num_of_tweets)
        

