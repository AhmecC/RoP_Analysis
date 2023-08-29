import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



### --- WORDCLOUDS --- ###
### >>> Across all subreddits we see that the Main Characters (Galadriel & Halbrand) were mentioned alot
### >>> Sauron was mentionited alot despite not being in the show till the least episode
### >>> 'S' is used to denote sarcasm which we see is quite prevalent across all subreddits
from wordcloud import WordCloud, STOPWORDS
my_stopwords = ['show', 'episode', 'think', 'one', 'make', 'people', 'know', 'scene', 'really', 'see', 'think', 'thing', 'will']
STOPWORDS.update(my_stopwords)

# >>> r/LOTR_on_Prime
comment_corpus = ''.join(LOTR_on_Prime['Comment'])
LOTR_on_Prime_comment = WordCloud(stopwords=STOPWORDS).generate(comment_corpus)
plt.imshow(LOTR_on_Prime_comment);
plt.title('r/LOTR_on_Prime Wordcloud');

# >>> r/lotr
comment_corpus2 = ''.join(lotr['Comment'])
lotr_comment = WordCloud(stopwords=STOPWORDS).generate(comment_corpus2)
plt.imshow(lotr_comment);
plt.title('r/lotr Wordcloud');

# >>> r/lordoftherings
comment_corpus3 = ''.join(lordoftherings['Comment'])
lordoftherings_comment = WordCloud(stopwords=STOPWORDS).generate(comment_corpus3)
plt.imshow(lordoftherings_comment);
plt.title('r/lordoftherings Wordcloud');

# >>> r/RingsofPower
comment_corpus4 = ''.join(RingsofPower['Comment'])
RingsofPower_comment = WordCloud(stopwords=STOPWORDS).generate(comment_corpus4)
plt.imshow(RingsofPower_comment);
plt.title('r/RingsofPower Wordcloud');

# >>> r/Rings_Of_Power
comment_corpus5 = ''.join(Rings_Of_Power['Comment'])
Rings_Of_Power_comment = WordCloud(stopwords=STOPWORDS).generate(comment_corpus5)
plt.imshow(Rings_Of_Power_comment);
plt.title('r/Rings_Of_Power Wordcloud');








### --- Sentiment Analysis --- ###
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
vds = SentimentIntensityAnalyzer()


### --- Work out Sentiment scores from (-1,1) --- ###
Rings_Of_Power['Sentiment'] = Rings_Of_Power['Comment'].apply(lambda x: vds.polarity_scores(x)['compound'])
RingsofPower['Sentiment'] = RingsofPower['Comment'].apply(lambda x: vds.polarity_scores(x)['compound'])
LOTR_on_Prime['Sentiment'] = LOTR_on_Prime['Comment'].apply(lambda x: vds.polarity_scores(x)['compound'])
lotr['Sentiment'] = lotr['Comment'].apply(lambda x: vds.polarity_scores(x)['compound'])
lordoftherings['Sentiment'] = lordoftherings['Comment'].apply(lambda x: vds.polarity_scores(x)['compound'])


### --- Plot Sentiment out per Episode & Subreddit -- ###
# >>> There seems to be a downwards trend in how positive subreddits are overall with the show's episodes
# >>> Episode 4 seemed to resonate with r/lotr and r/LOTR_on_Prime whilst being the opposite for r/lordoftherings
# >>> Despite being the highest rated episode, there is no increase in sentiment for Episode 6 (it is actually on of the lowest for most subreddits
# >>> r/Rings_Of_Power is the most negative overall whilst r/LOTR_on_Prime and r/ringsofpower are the most positive
plt.figure(figsize=(10,6))
plt.plot(lordoftherings.groupby('Episode').mean(numeric_only=True)['Sentiment'], label='lordoftherings');
plt.plot(lotr.groupby('Episode').mean(numeric_only=True)['Sentiment'], label='lotr');
plt.plot(LOTR_on_Prime.groupby('Episode').mean(numeric_only=True)['Sentiment'], label='LOTR_on_Prime');
plt.plot(RingsofPower.groupby('Episode').mean(numeric_only=True)['Sentiment'], label='RingsofPower');
plt.plot(Rings_Of_Power.groupby('Episode').mean(numeric_only=True)['Sentiment'], label='Rings_Of_Power');
plt.legend();








### --- Weighted Sentiment Analysis --- ###
def sigmoid(u, kappa=0.1, theta=0):
    return 1 / (1 + np.exp(-kappa * (u - theta)))

def adjust_sentiment_v3(row):
    s = row['Sentiment']
    u = row['Comment Upvotes']
    if abs(u) >= 20:
        # For high upvotes, pull sentiment towards extremes
        weight = sigmoid(u)
        return np.sign(s) * (np.abs(s) + (1 - np.abs(s)) * weight)
    else:
        # For low upvotes, pull sentiment towards 0
        weight = sigmoid(5 - abs(u))
        return np.sign(s) * (np.abs(s) * (1 - weight))

LOTR_on_Prime['Weighted Sentiment'] = LOTR_on_Prime.apply(adjust_sentiment_v3, axis=1)
lotr['Weighted Sentiment'] = lotr.apply(adjust_sentiment_v3, axis=1)
lordoftherings['Weighted Sentiment'] = lordoftherings.apply(adjust_sentiment_v3, axis=1)
Rings_Of_Power['Weighted Sentiment'] = Rings_Of_Power.apply(adjust_sentiment_v3, axis=1)
RingsofPower['Weighted Sentiment'] = RingsofPower.apply(adjust_sentiment_v3, axis=1)


### --- Plot Weighted Sentiment out per Episode & Subreddit -- ###
plt.figure(figsize=(10,6))
plt.plot(lordoftherings.groupby('Episode').mean(numeric_only=True)['Weighted Sentiment'], label='lordoftherings');
plt.plot(lotr.groupby('Episode').mean(numeric_only=True)['Weighted Sentiment'], label='lotr');
plt.plot(LOTR_on_Prime.groupby('Episode').mean(numeric_only=True)['Weighted Sentiment'], label='LOTR_on_Prime');
plt.plot(RingsofPower.groupby('Episode').mean(numeric_only=True)['Weighted Sentiment'], label='RingsofPower');
plt.plot(Rings_Of_Power.groupby('Episode').mean(numeric_only=True)['Weighted Sentiment'], label='Rings_Of_Power');
plt.title('Weighted Sentiment per Subreddit per Episode')
plt.legend();





