#importing all necessary modules
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import json
import csv
from functools import reduce
import operator

def read_json_file(filename):
    f = open(filename, 'r')
    data = json.load(f)
    f.close()
    return data

words_list = read_json_file("filtered_tweet_words.json")
text = ' '.join(words_list)

wordcloud = WordCloud(width = 800, height = 800,
				background_color ='white',
				min_font_size = 10).generate(text)

# plot the WordCloud image					
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()