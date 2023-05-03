#Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt

#importanting data frames
twitter_data = pd.read_csv("Twitter_Data.csv")
twitter_data.head()
reddit_data = pd.read_csv("Reddit_Data.csv")
reddit_data.head()

def save_to_json_file(obj, filename):
    f = open(filename, 'w')
    json.dump(obj, f)
    f.close()

# Turn Each Data Entry Into Python List 
tweets = twitter_data['clean_text'].tolist()
#print(tweets)
reddit_posts = reddit_data['clean_comment'].tolist()
#print(reddit_posts)

# Turn List of Tweet Strings Into List of Indv. Words 
from functools import reduce
import json
import operator 
print('before string conversion:', len(tweets))
tweets = [str(i) for i in tweets]
print('after string conversion:', len(tweets))
words = reduce(lambda acc, cur: acc + cur.split(), tweets, [])
print('words after reduce:', len(tweets))
save_to_json_file(words, 'tweet_words.json')


#DOMO ZONO *sammi do not delete, but also sammi do not understand*
# %matplotlib inline
# from wordcloud import WordCloud
# #Importing Dataset
# df = pd.read_csv("android-games.csv")
# #Checking the Data
# df.head()
# #Checking for NaN values
# df.isna().sum()
# #Removing NaN Values
# df.dropna(inplace = True)
# #Creating the text variable
# text = " ".join(cat.split()[1] for cat in df.category)
# # Creating word_cloud with text as argument in .generate() method
# word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
# # Display the generated Word Cloud
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()