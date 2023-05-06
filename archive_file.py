##IMPORTANT MAY & DOMO DO NOT RUN THIS CODE IT WILL MELT YOUR COMPUTER
## ALL YOU NEED TO ACCESS IS REDDIT_WORD.JSON FILE & THE 
## The code below creates two json files containing the individual words from each tweet/reddit post 

# Importing Libraries 
import pandas as pd

# Function later used to create JSON Files 
def save_to_json_file(obj, filename):
    f = open(filename, 'w')
    json.dump(obj, f)
    f.close()

# Importing Data Frames 
reddit_data = pd.read_csv("Reddit_Data.csv")
twitter_data = pd.read_csv("Twitter_Data.csv")

# Turn Each Post Into Python List 
reddit_posts = reddit_data['clean_comment'].tolist()
tweets = twitter_data['clean_text'].tolist()

# Turn Each List Into New JSON File of each ind. Word
from functools import reduce
import json
import operator 
print('before string conversion:', len(reddit_posts))
reddit_posts = [str(i) for i in reddit_posts]
print('after string conversion:', len(reddit_posts))
words = reduce(lambda acc, cur: acc + cur.split(), reddit_posts, [])
print('words after reduce:', len(reddit_posts))
save_to_json_file(words, 'reddit_words.json')

print('before string conversion:', len(tweets))
tweets = [str(i) for i in tweets]
print('after string conversion:', len(tweets))
words = reduce(lambda acc, cur: acc + cur.split(), tweets, [])
print('words after reduce:', len(tweets))
save_to_json_file(words, 'tweet_words.json')


