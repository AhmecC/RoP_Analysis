import praw
from praw.models import MoreComments
import pandas as pd

### --- Sensitive Info --- ###
client_id = ''
secret = ''
username = ''
password = ''



### --- Connecting to Reddit API --- ###
reddit = praw.Reddit(client_id = client_id,
                     client_secret = secret,
                     password = password,
                     user_agent = 'MyBot/0.0.1',
                     username = username)



### --- Script to find Fullname of Megathread --- ###
# ^^ Note i ended up finding the id myself by searching reddit, but this functionality is still helpful

sub = reddit.subreddit('lotr')  # Subreddit to search through
posts = sub.top(time_filter = 'all', limit = None)  # Returns all top posts
posts_dict = {'Fullname':[], 'Title':[],'Created On':[]}

start_date = datetime.datetime.strptime('01-09-22 00:00:00', '%d-%m-%y %H:%M:%S').timestamp()  # Range to search top posts from
end_date = datetime.datetime.strptime('03-09-22 00:00:00', '%d-%m-%y %H:%M:%S').timestamp()

for x in posts:
    date =  x.created_utc  # Date of post creation    
    if date > start_date and date < end_date:
        posts_dict['Fullname'].append(x.fullname)
        posts_dict['Title'].append(x.title)
        posts_dict['Created On'].append(x.created_utc)
df = pd.DataFrame(posts_dict)  # Return info in dataframe



### --- ID's of Megathread for each Subreddit --- ###
LOTR_on_Prime = {'x3nsjx':1, 'x3o09c':2, 'x9hxch':3, 'xf5qin':4, 'xkkk4n':5 ,'xrdgqy':6, 'xxavcr':7, 'y343kq':8} 
lotr = {'x3nlz8':12, 'x9kz54':3, 'xfgpxi':4, 'xlmna8':5, 'xrrh9j':6, 'xxour1':7, 'y3ja6b':8}
RingsofPower = {'x3qfqz':12, 'x9ngqa':3, 'xfgx9y':4, 'xlmurh':5, 'xrrbtm':6, 'xxoyvo':7, 'y3j23u':8}
lordoftherings = {'x3jxjt':12, 'x8bikm':3, 'xf7ucr':4, 'xl5rge':5, 'xqzk70':6, 'xx4ly7':7, 'y2pjap':8}



### --- Script to obtain many comments from megathread --- ###
def get_comments(ID):]
    comment = []
    value = lotr.get(ID)  # Get Episode Number for specific dictionary
    
    submission = reddit.submission(ID)
    submission.comments.replace_more(limit=75)
    for x in submission.comments.list():
        comment.append(['lotr', ID, value, x.body, x.score])  # return subreddit name, thread ID, episode number, Comment Content & Upvotes
    return comment

df_lotr = pd.DataFrame()  # Create dataframe for each subreddit
for x in lotr:
    comment = get_comments(x)
    df_lotr = df_lotr.append(comment, ignore_index=True)
    print('Complete')
df_lotr = df_lotr.rename(columns={0:'Subreddit', 1:'Fullname ID', 2:'Episode', 3:'Comment', 4:'Comment Upvotes'})



### --- Save all dataframes --- ###
df_lordoftherings.to_csv('r_lordoftherings')
df_RingsofPower.to_csv('r_RingsofPower')
df_lotr.to_csv('r_lotr')
df_LOTR_on_Prime.to_csv('r_LOTR_on_Prime')


















