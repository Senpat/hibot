#says hi when someone says hi to me

#from bs4 import BeautifulSoup
#from urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4

path = "/Users/zz198/Desktop/PatrickP/Bot/commented.txt"

def authenticate():
  print("Authenticating...\n")
  #reddit = praw.Reddit('hibot',user_agent = 'web:hi-bot:v0.1 (by /u/The_Senpat)')
  reddit = praw.Reddit(client_id='P6KBJamDVskaOQ',
                     client_secret="KhlUmoWTy21NVtHtbPEmAT1mBv4", password='bot1password',
                     user_agent='hibot by /u/TheSenpat', username='spbot1')
  print('Authenticated as {}\n'.format(reddit.user.me()))
  return reddit

def run_hibot(reddit):
    print('getting 250 comments...\n')
    
    for comment in reddit.subreddit('test').comments(limit = 250):
        if "hi TheSenpat" in comment.body:
            print('Link found with comment ID: ' + comment.id)
            
            #check to see if comment id is in the file
            file_obj_r = open(path,'r')
    
            if comment.id not in file_obj_r.read().splitlines():
                print('Link is unique...posting explanation\n')
                comment.reply(header + explanation + footer)                 
                file_obj_r.close()

                file_obj_w = open(path,'a+')
                file_obj_w.write(comment.id + '\n')
                file_obj_w.close()
            else:
                print('Already visited link...no reply needed\n')
            
            comment.reply('hi')
            
            time.sleep(60)
            
            
def main():
    print("main2")
    reddit = authenticate()
    print("main3")
    while True:
        run_hibot(reddit)
      
if __name__ == '__main__':
    print("main1")
    main()
