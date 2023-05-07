##IMPORTANT MAY & DOMO DO NOT RUN THIS CODE IT WILL MELT YOUR COMPUTER
## ALL YOU NEED TO ACCESS IS REDDIT_WORD.JSON FILE & THE 
## The code below creates two json files containing the individual words from each tweet/reddit post 

# # Importing Libraries 
import pandas as pd
from functools import reduce
import json
import operator 

# # Function landing pad 
def save_to_json_file(obj, filename):
    f = open(filename, 'w')
    json.dump(obj, f)
    f.close()

# def article_filter(df):
#     articles = ['a', 'an', 'the', 'it', 'is', 'its', 'they', 'them', 'their', 'our', 'all', 'any', 'another', 'I', 'both', 'each','we'
#                 'us','some', 'anything', 'these', 'he', 'him', 'she', 'most', 'you', 'her', 'others', 'himself', 'where', 'whose', 'your']
#     if ( in articles):
#         return False
#     else:
#         return True



# # Importing Data Frames 
# reddit_data = pd.read_csv("Reddit_Data.csv")
# twitter_data = pd.read_csv("Twitter_Data.csv")

# # Turn Each Post Into Python List 
# reddit_posts = reddit_data['clean_comment'].tolist()
# tweets = twitter_data['clean_text'].tolist()


# # Turn Each List Into New JSON File of each ind. Word

# print('before string conversion:', len(reddit_posts))
# reddit_posts = [str(i) for i in reddit_posts]
# print('after string conversion:', len(reddit_posts))
# words = reduce(lambda acc, cur: acc + cur.split(), reddit_posts, [])
# print('words after reduce:', len(reddit_posts))
# save_to_json_file(words, 'reddit_words.json')

# print('before string conversion:', len(tweets))
# tweets = [str(i) for i in tweets]
# print('after string conversion:', len(tweets))
# words = reduce(lambda acc, cur: acc + cur.split(), tweets, [])
# print('words after reduce:', len(tweets))
# save_to_json_file(words, 'tweet_words.json')

# # Filtering Each JSON File to Eliminate Articles

tweet_words_json = pd.read_json('tweet_words.json')
articles = ['a', 'an', 'the', 'it', 'is', 'its', 'they', 'them', 'their', 'our', 'all', 'any', 'another', 'I', 'both', 'each','we'
'us','some', 'anything', 'these', 'he', 'him', 'she', 'most', 'you', 'her', 'others', 'himself', 'where', 'whose', 'your']
filtered_tweet_words = reduce(lambda acc, curr,: if curr in articles  ,  tweet_words_json)
save_to_json_file(filtered_tweet_words, 'filtered_tweet_words.json')


# for item in tweet_words_json:
#     if item not in articles:
#         tweet_words_json.append(item)
# print(tweet_words_json)
        





## filtered words into a file 
# tweet_words_json = pd.read_json('tweet_words.json')
# filtered = filter(article_filter, tweet_words_json)
# print(reduce(filter(article_filter, tweet_words_json), tweet_words_json))
# for articles in filtered:
#     print(filtered)
    # save_to_json_file(filtered, 'tweet_words_filtered.json')




## Sammi's save for later code 

## func to filter out words (chosing not to use bc reduce does this)


