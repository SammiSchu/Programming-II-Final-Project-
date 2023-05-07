# Programming-II-Final-Project-

## Libraries we Utilized
``` 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import json
import csv
from functools import reduce
import operator 
```
## Processing Data 
### Data Management
```
def read_json_file(filename):
    f = open(filename, 'r')
    data = json.load(f)
    f.close()
    return data
``` 
* json.load -> used to read the JSON document from python 
    - converts the JSON string document into a Python dictionary 
    - helps retrive the data from JSON to python
    
### Word Cloud Code

```
words_list = read_json_file("filtered_tweet_words.json")
text = ' '.join(words_list)

wordcloud = WordCloud(width = 800, height = 800,
				background_color ='white',
				min_font_size = 10).generate(text)
```
* Takes all the elements and joins them into a single string of data in order to plot the data cloud 

### Word Cloud Image 
```
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
``` 

 > Here is our Reddit wordcloud:
![reddit_wordcloud](images/reddit_word_cloud.png)

 > Here is our Twitter wordcloud:
![python_wordcloud](images/twitter_word_cloud.png)




## Favorite Piece of Code

## Adom 

One part of the code that I particularly enjoyed was when we used the NLTK package to filter a massive list of words and create a JSON file of strings that contained only the words we wanted to include in our final word cloud. Using this package was incredibly helpful, saving us a lot of time and sparing us from the need for extensive logical thinking. Our success with NLTK is a testament to our team's hard work and our growing proficiency with Python, libraries, and documentation. Without NLTK, we would have spent an unnecessary amount of time on a task that ultimately took only minutes to complete.

## Sammi 


## Maya 

My favorite piece of code was the mechanics of the word cloud generator itself. We imported matplotlib.pyplot as plt which is an interface to the matplot library. The .pyplot opens the figure word cloud on the screen and acts as the figure GUI manager with the interactive plot. The library is interesting as it's a multi-platform data visualization library built on arrays to be used for interactive plots and programmatic plot generation. The library made it very easy to visualize and manipulate any details of the plot. 

    

