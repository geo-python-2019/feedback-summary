"""
Plot wordclouds based on this data camp tutorial: https://www.datacamp.com/community/tutorials/wordcloud-python

"""
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

def plot_word_cloud(text):
    """Plot word cloud. Based on this data camp tutorial: https://www.datacamp.com/community/tutorials/wordcloud-python"""
    
    # Create stopword list:
    stopwords = set(STOPWORDS)
    #stopwords.update([])

    # Generate a word cloud image
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    
    # Create and generate a word cloud image:    
    #wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

    # Display the generated image:
    plt.figure(figsize=[12,12])
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()