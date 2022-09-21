import datetime
import praw
import pandas as pd

def isImage(post):
    try:
        return post.post_hint=='image'
    except AttributeError:
        return False

def getImageURLs(client: praw.Reddit,subreddit_name: str,limit:int):
    hot_memes = client.subreddit(subreddit_name).hot(limit=limit)
    posts = []
    for post in hot_memes:
        if(isImage(post)):
            posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, datetime.datetime.fromtimestamp(post.created)])
    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    
    posts.to_csv(f"subreddits-csv/{subreddit_name}.csv", index=True)

if __name__ == "__main__":
    client = praw.Reddit(
        client_id="id",
        client_secret="secret-key",
        password="password",
        user_agent="bot-name",
        username="username"
    )
    subreddit_name = "sub-name"
    getImageURLs(client, subreddit_name, limit=1000)