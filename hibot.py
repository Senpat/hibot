#says hi when someone says hi to me

from bs4 import BeautifulSoup
from urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4

def authenticate():
  print("Authenticating...\n")
  reddit = praw.Reddit('hibot',user_agent = 'web:hi-bot:v0.1 (by /u/The_Senpat)')
  print('Authenticated as {}\n'.format(reddit.user.me()))
  return reddit

def run_hibot(reddit):
    print('getting 250 comments...\n')
    
    for comment in reddit.subreddit('test').comments(limit = 250):
        if "hi TheSenpat" in comment.body:
            print('Link found with comment ID: " + comment.id')
            
            #check to see if comment id is in the file
            
            comment.reply('hi')
            
            time.sleep(60)
            
            
def main():
    reddit = authenticate()
    while True:
        run_hibot(reddit)
      
if __name__ == '__main__':
    main()
