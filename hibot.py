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
  
  
