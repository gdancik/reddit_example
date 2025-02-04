import praw
import credentials as cred
id = cred.id
secret = cred.secret

reddit = praw.Reddit(client_id=id, client_secret=secret, user_agent="my user agent")

for submission in reddit.subreddit('learnpython').hot(limit=10):
        print(submission.title)



