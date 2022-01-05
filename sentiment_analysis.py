import os
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS

sia = SentimentIntensityAnalyzer()


def combine_df(directory):

    frames = []

    # read all csv files in 'output' folder
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".csv"):
                frames.append(pd.read_csv(root + "/" + filename))

    return pd.concat(frames)['tweet']  # get all the 'tweets' and append to df


def piechart_sentiment(counts):
    mask = plt.Circle((0, 0), 0.7, color="white")
    plt.pie(counts, labels=["Positive", "Negative",
            "Neutral"], colors=['green', 'blue', 'red'])
    plt.legend(["Positive", "Negative", "Neutral"])
    plt.title("Sentiment Analysis Result")
    p = plt.gcf()
    p.gca().add_artist(mask)
    plt.show()


def is_positive(tweet):
    return sia.polarity_scores(tweet)

'''
Takes df as input and returns the % of 'positive' tweets.
'''
def sentiment_analysis(t):
    total = 0
    positive = 0
    negative = 0
    neutral = 0
    for index, row in t["text"].items():
        tweet = row
        total += 1
        score = is_positive(tweet)
        if score['neg'] > score['pos']:
            t.loc[index, 'sentiment'] = 'negative'
            negative += 1

        elif score['pos'] > score['neg']:
            t.loc[index, 'sentiment'] = 'positive'
            positive += 1
        else:
            t.loc[index, 'sentiment'] = 'neutral'
            neutral += 1

    # display results as a pie chart
    #piechart_sentiment([positive, negative, neutral])

    return (positive / total, negative / total, neutral / total)


def clean_data(df):
    # remove duplicate tweets
    df.drop_duplicates(inplace=True)

    # Creating new dataframe and new feature/column to work on
    tw_list = pd.DataFrame(df)
    tw_list["text"] = tw_list["tweet"]

    # Removing RT, Punctuation etc
    words = ["Huawei", "5G", "cyber security", "cybersecurity", "China Canada trade", "Canada China trade", "https", "Canada China relationship", "China Canada relationship"]
    stopwords = " ".join(words)
    def remove_rt(x): return re.sub("RT @\w+: ", " ", x)
    pattern = re.compile(r'(https?://)?(www\.)?(\w+\.)?(\w+)(\.\w+)(/.+)?')
    def rthttp(x): return re.sub(pattern,'',x)
    def rtx(x): return re.sub('[!@#$:).;,?&]', '', x.lower())
    def rty(x): return re.sub('  ', ' ', x)
    def rwords(x): return re.sub(stopwords, "", x)
    tw_list["text"] = tw_list.text.map(rthttp).map(remove_rt).map(rtx).map(rty)
    return tw_list


def wordcloud(df, col):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(max_font_size=50, background_color="white",
                          stopwords=stopwords).generate(" ".join([i for i in df[col]]))
    plt.figure(figsize=(20, 10), facecolor='k')
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud")
    wordcloud.to_file("output/cloud.png")
    # plt.show()


if __name__ == '__main__':
    df = combine_df("output")
    clean_df = clean_data(df)

    wordcloud(clean_df, 'text')
    # print(sentiment_analysis(clean_df))
