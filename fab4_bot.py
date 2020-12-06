import praw
from urllib.parse import quote_plus
import os

reddit = praw.Reddit(
    user_agent="Fab4 Bot",
    client_id="bYUjhuL-6FA_mg",
    client_secret="j6rxSyrIASuayUlE05QtUcnF8wMw8A",
    username="fab4-bot",
    password="password2003"
)

copypasta = '''
The Fab 4 was actually a creation by the late Martin Crowe, who wrote an article in the mid 2010s about four young batsmen who were destined to lead their respective countries in the future. It's not a something you can just 'join'; it's an exclusive club for these four cricketers.
\n\nYou can find the article [here](https://www.espncricinfo.com/story/_/id/21431212/test-cricket-young-fab-four).
'''

keywords = {'fab':['fab4', 'fab5', 'fab 4', 'fab 5'], 'babar':['babar azam', 'azam', 'babar']}

def main():
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = list(filter(None, f.read().split("\n")))
        
    subreddit = reddit.subreddit('pythonforengineers')
    for submission in subreddit.stream.submissions(pause_after=-1):
        if submission.id not in posts_replied_to and submission is not None:
            if check_text_for_keywords(submission.title):
                submission.reply(copypasta)
                posts_replied_to.append(submission.id)
    for comment in subreddit.stream.comments(pause_after=-1):
        if comment.id not in posts_replied_to and comment is not None:
            if check_text_for_keywords(comment.body):
                comment.reply(copypasta)
                posts_replied_to.append(comment.id)
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

def check_text_for_keywords(text):
    fab, babar = False, False
    for i in keywords['fab']:
        if i in text.lower():
            fab = True
    for j in keywords['babar']:
        if j in text.lower():
            babar = True  
    return (fab and babar)

if __name__ == '__main__':
    main()