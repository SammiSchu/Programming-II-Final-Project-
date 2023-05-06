#importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import json
import csv
from functools import reduce
import operator

def save_to_json_file(obj, filename):
    f = open(filename, 'w')
    json.dump(obj, f)
    f.close()

# with open('tweet_words.json', encoding = 'utf-8') as inputfile:
#     tweet_words = pd.read_json(inputfile)
# tweet_words.to_csv('tweet_words.csv', encoding = 'utf-8', index = False)
# tweet_words = [str(i) for i in "tweet_words.csv"]

def article_filter(df):
    articles = ['a', 'an', 'the', 'it', 'is', 'its', 'they', 'them', 'their', 'our', 'all', 'any', 'another', 'I', 'both', 'each','we'
                'us','some', 'anything', 'these', 'he', 'him', 'she', 'most', 'you', 'her', 'others', 'himself', 'where', 'whose', 'your']
    if (df in articles):
        return True
    else:
        return False
    
## attempting to save filtered words into a file 
tweet_words_json = pd.read_json('tweet_words.json')
filtered = filter(article_filter, tweet_words_json)
for articles in filtered:
    print(filtered)
    # save_to_json_file(filtered, 'tweet_words_filtered.json')

# Reads 'Youtube04-Eminem.csv' file
# df = pd.read_json("tweet_words.json")
# df = pd.read_json('reddit_words.json')
# df = df.to_csv('reddit_words.json')
# df = [str(i) for i in df]
# df.describe()

# df = tweet_words

# comment_words = ''
# stopwords = set(STOPWORDS)

# # iterate through the csv file
# for val in df:
	
# 	# typecaste each val to string
# 	val = str(val)

# 	# split the value
# 	tokens = val.split()
	
# 	# Converts each token into lowercase
# 	for i in range(len(tokens)):
# 		tokens[i] = tokens[i].lower()
	
# 	comment_words += " ".join(tokens)+" "

# wordcloud = WordCloud(width = 800, height = 800,
# 				background_color ='white',
# 				stopwords = stopwords,
# 				min_font_size = 10).generate(comment_words)

# # plot the WordCloud image					
# plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad = 0)

# plt.show()

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