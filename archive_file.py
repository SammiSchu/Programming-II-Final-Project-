##IMPORTANT MAY & DOMO DO NOT RUN THIS CODE IT WILL MELT YOUR COMPUTER
## ALL YOU NEED TO ACCESS IS REDDIT_WORD.JSON FILE & THE 
## The code below creates two json files containing the individual words from each tweet/reddit post 

# # Importing Libraries 
import pandas as pd
from functools import reduce
import json
import operator
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

def save_to_json_file(obj, filename):
    f = open(filename, 'w')
    json.dump(obj, f)
    f.close()


def read_json_file(filename):
    f = open(filename, 'r')
    data = json.load(f)
    f.close()
    return data


# Importing Data Frames 
reddit_data = pd.read_csv("Reddit_Data.csv")
twitter_data = pd.read_csv("Twitter_Data.csv")

# Turn Each Post Into Python List 
reddit_posts = reddit_data['clean_comment'].tolist()
tweets = twitter_data['clean_text'].tolist()


# Turn Each List Into New JSON File of each ind. Word

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

# Filtering Each JSON File to Eliminate Articles

tweet_words_json = read_json_file('tweet_words.json')
reddit_words_json =read_json_file('reddit_words.json')

# Filtering out articles using NLTK
# Using nltk, we can tag each word with the part of speech
# see https://www.nltk.org/book/ch05.html#tab-universal-tagset
tagged_tweet_words = nltk.pos_tag(tweet_words_json, tagset='universal')
parts_not_wanted = ['PRON', 'ADP', 'ADV', 'CONJ', 'DET', 'PRT', '.']
twitter_filtered = [w for w in tagged_tweet_words if w[1] not in parts_not_wanted]
# turn back into a regular list of words
filtered_tweet_words = [w[0] for w in twitter_filtered]
save_to_json_file(filtered_tweet_words, 'filtered_tweet_words.json')

tagged_reddit_words = nltk.pos_tag(reddit_words_json, tagset='universal')
reddit_filtered = [w for w in tagged_reddit_words if w[1] not in parts_not_wanted]
# turn back into a regular list of words
filtered_reddit_words = [w[0] for w in reddit_filtered]
save_to_json_file(filtered_reddit_words, 'filtered_reddit_words.json')

