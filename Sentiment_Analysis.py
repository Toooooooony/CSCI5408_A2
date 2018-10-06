from textblob import TextBlob
import csv
import re

tweets = []

def clean(input):
    input = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', input)
    input = re.sub(r'\bwth\b', 'what the hell', input)
    input = re.sub(r'\br\b', 'are', input)
    input = re.sub(r'\bu\b', 'you', input)
    input = re.sub(r'\bk\b', 'OK', input)
    input = re.sub(r'\bsux\b', 'sucks', input)
    input = re.sub(r'\bno+\b', 'no', input)
    input = re.sub(r'\bcoo+\b', 'cool', input)
    input = re.sub(r'\bthats\b', 'that is', input)
    input = re.sub(r'\bive\b', 'i have', input)
    input = re.sub(r'\bim\b', 'i am', input)
    input = re.sub(r'\bya\b', 'yeah', input)
    input = re.sub(r'\bcant\b', 'can not', input)
    input = re.sub(r'\bwont\b', 'will not', input)
    input = re.sub(r'\bid\b', 'i would', input)
    input = re.sub(r'wtf', 'what the fuck', input)
    input = re.sub(r'rip', 'rest in peace', input)
    input = re.sub(r'lol', 'laugh out loud', input)
    input = re.sub(r'lmao', 'laughing my ass off', input)
    
    return input

with open('tweets.csv', newline='',encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        tweet = dict()
        tweet['id'] = row[0]
        tweet['user'] = row[1]
        tweet['created_at'] = row[2]
        tweet['text'] = clean(row[3])
        tweet['TextBlob'] = TextBlob(tweet['text'])
        tweets.append(tweet)

for tweet in tweets:
    tweet['polarity'] = float(tweet['TextBlob'].sentiment.polarity)

    if tweet['polarity'] > 0.2:
        tweet['sentiment'] = 'positive'
    elif tweet['polarity'] < -0.2:
        tweet['sentiment'] = 'negative'
    else:
        tweet['sentiment'] = 'neutral'

with open ('tweets_result.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['tweet', 'sentiment ', 'sentiment_score'])
    for x in range(1,len(tweets)):
        writer.writerow([tweets[x]['text'],tweets[x]['sentiment'],tweets[x]['polarity']])

print("Done!")
