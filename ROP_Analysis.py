### --- HOUSEKEEPING --- ###
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

LOTR_on_Prime = pd.read_csv('r_LOTR_on_Prime')
lotr = pd.read_csv('r_lotr')
lordoftherings = pd.read_csv('r_lordoftherings')
RingsofPower = pd.read_csv('r_RingsofPower')
Rings_Of_Power = pd.read_csv('r_Rings_Of_Power')


### --- Rename Episodes --- ###
episode_mapping = {1:'Episode 1 & 2', # Join Episode 1/2 together since 4/5 subreddits have a joint megathread
                   2: 'Episode 1 & 2',
                   3: 'Episode 3',
                  4: 'Episode 4',
                  5: 'Episode 5',
                  6: 'Episode 6',
                  7: 'Episode 7',
                  8: 'Episode 8',
                  12: 'Episode 1 & 2'}

LOTR_on_Prime['Episode'] = LOTR_on_Prime['Episode'].map(episode_mapping)
lotr['Episode'] = lotr['Episode'].map(episode_mapping)
lordoftherings['Episode'] = lordoftherings['Episode'].map(episode_mapping)
RingsofPower['Episode'] = RingsofPower['Episode'].map(episode_mapping)
Rings_Of_Power['Episode'] = Rings_Of_Power['Episode'].map(episode_mapping)




### EDA 




### --- Total scraped comments per episode 
# >>> Seems to be overall upwards trend in comments except r/lordoftherings who were constant
# >>> Highest rated Episode (6) seemed to cause a spike in engagement aswell as the finale
plt.figure(figsize=(10,6))
plt.plot(LOTR_on_Prime.groupby('Episode').count()['Comment'], label = 'r/LOTR_on_Prime');
plt.plot(lordoftherings.groupby('Episode').count()['Comment'], label = 'r/lordoftherings')
plt.plot(lotr.groupby('Episode').count()['Comment'], label ='r/lotr')
plt.plot(RingsofPower.groupby('Episode').count()['Comment'], label = 'r/RingsofPower')
plt.plot(Rings_Of_Power.groupby('Episode').count()['Comment'], label = 'r/Rings_of_Power')
plt.title('Comments per Episode')
plt.legend();




### --- Episode Ratings
# >>> Episodes started off decent (7.3 average) but soon started to fall off (lowest 6.8)
# >>> Jump for Episode 6 (highest rated episode) and then dropped to lowest in Episode 7
# >>> Second highest rated was finale
episode_ratings = [
                  ['Episode 1', 'A Shadow of the Past', 7.3, 52100],
                  ['Episode 2', 'Adrift', 7.4, 47768],
                  ['Episode 3', 'Adar', 7.3, 34927],
                  ['Episode 4', 'The Great Wave', 7.1, 28853],
                  ['Episode 5', 'Partings', 6.8, 25584],
                  ['Episode 6', 'Udun', 8.2, 33525],
                  ['Episode 7', 'The Eye', 6.6, 23617],
                  ['Episode 8', 'Alloyed', 7.8, 26430]
                  ]

episode_ratings = pd.DataFrame(episode_ratings, columns=['Episode', 'Title', 'IMDB Rating', 'IMDB Reviews'])

plt.figure(figsize=(10,6))
plt.plot(episode_ratings.Episode, episode_ratings['IMDB Rating'])
plt.title('Episode IMDB Ratings');




### --- Episode Number of Reviews
# >>> Number of reviews fell off as show went on, but small spikes for highest rated episodes
# >>> Engagement seems to have fallen off as the show went on
plt.figure(figsize=(10,6))
plt.plot(episode_ratings.Episode, episode_ratings['IMDB Reviews'])
plt.title('Number of Reviews per Episode');




### --- Negative Upvotes per Comment
# >>> Most comments have 0-5 upvotes within subreddits
# >>> r/LOTR_on_Prime had the most negative upvoted comments (followed by r/lotr)
# >>> r/lordoftherings had the least negative upvoted comments (community seems to be strong)
# >> r/RingsofPower and r/Rings_Of_Power had comments with very high downvotes (>-20)
fig, axes = plt.subplots(2,3, figsize=(10,6))

sns.histplot(data=LOTR_on_Prime, x='Comment Upvotes', bins=250, ax=axes[0,0])
axes[0][0].set_xlim(-30,30)
axes[0][0].set_title('r/LOTR_on_Prime')

sns.histplot(data=lotr, x='Comment Upvotes', bins=300, ax=axes[0,1])
axes[0][1].set_xlim(-30,30)
axes[0][1].set_title('r/lotr')

sns.histplot(data=lordoftherings, x='Comment Upvotes', bins=200, ax=axes[0,2])
axes[0][2].set_xlim(-30,30)
axes[0][2].set_title('r/lordoftherings')

sns.histplot(data=RingsofPower, x='Comment Upvotes', bins=50, ax=axes[1,0])
axes[1][0].set_xlim(-30,30)
axes[1][0].set_title('r/RingsofPower')

sns.histplot(data=Rings_Of_Power, x='Comment Upvotes', bins=50, ax=axes[1,1])
axes[1][1].set_xlim(-30,30)
axes[1][1].set_title('r/Rings_Of_Power')
plt.tight_layout();




### --- Subreddit Growth as episodes released
# >>> r/LOTR_on_Prime doubled and nearly overtook r/lordoftherings in the timeframe
# >>> r/Rings_of_Power was the smallest and had stagnant growth, whilst r/RingsofPower grew a fair amount
growth_data = [
    ['September 1st', 5109, 73186, 165482, 683898, 2750],
    ['September 9th', 16524, 104969, 172126, 701368, 7219],
    ['September 16th', 22031, 119253, 174707, 711370, 8363],
    ['September 23rd', 26682, 131518, 177155, 722910, 9407],
    ['September 30th', 31101, 143833, 178942, 731598, 10575],
    ['October 7th', 36210, 157799, 180266, 740541, 11875],
    ['October 14th', 40078, 172961, 181835, 749130, 13459 ],
    ['October 21st', 44428, 183905, 186723, 756721, 15000 ]] # Final date is a week after last episode dropped
growth_data = pd.DataFrame(growth_data, columns=['Date', 'RingsofPower', 'LOTR_on_Prime', 'Lordoftherings', 'lotr', 'Rings_Of_Power'])

plt.figure(figsize=(12,6))
plt.plot(growth_data.Date, growth_data.RingsofPower, label='r/RingsofPower')
plt.plot(growth_data.Date, growth_data.LOTR_on_Prime, label='r/LOTR_on_Prime')
plt.plot(growth_data.Date, growth_data.Lordoftherings, label='r/Lordoftherings')
plt.plot(growth_data.Date, growth_data.Rings_Of_Power, label='r/Rings_Of_Power')
plt.title('Subdreddit Followers Overtime')
plt.legend();




### --- Subreddit Percentage Growth as episodes released
# >>> Incumbent subreddits had low growth rate
# >>> r/LOTR_on_Prime and r/Rings_Of_Power had a high but consistent growth rate (10-15%)
# >>> r/RingsOfPower had highest growth rate but fell drastically overtime
percentage_increase = growth_data.set_index('Date').pct_change() * 100
percentage_increase = percentage_increase.drop('September 9th') # As obscenely high growth rate in some subreddits

plt.figure(figsize=(12,6))
plt.plot(percentage_increase.index, percentage_increase.RingsofPower, label='r/RingsofPower')
plt.plot(percentage_increase.index, percentage_increase.LOTR_on_Prime, label='r/LOTR_on_Prime')
plt.plot(percentage_increase.index, percentage_increase.Lordoftherings, label='r/Lordoftherings')
plt.plot(percentage_increase.index, percentage_increase.Rings_Of_Power, label='r/Rings_Of_Power')
plt.plot(percentage_increase.index, percentage_increase.lotr, label='r/lotr')
plt.title('Subdreddit Followers % Growth')
plt.legend();









