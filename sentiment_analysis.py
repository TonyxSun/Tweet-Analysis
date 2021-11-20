import pandas as pd
import os
from nltk.sentiment import SentimentIntensityAnalyzer


sia = SentimentIntensityAnalyzer()

def combine_df(directory):
    
    frames = []
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".csv"):
                frames.append(pd.read_csv(root + "/" + filename))
    
    return pd.concat(frames)['tweet']

def is_positive(tweet):
    return sia.polarity_scores(tweet)["compound"] > 0

def percent_postive(t):
    total = 0
    positive = 0
    for index, row in t.items():
        tweet = row
        total += 1
        if is_positive(tweet):
            positive += 1
    
    return positive / total
        

df = combine_df("output")
print (percent_postive(df))
    
    
    
    
    

    




