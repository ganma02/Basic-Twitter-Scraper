# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 13:32:44 2018
Using the Twitter Scraper
@author: win_8
"""

import pandas as pd
import scrape_twitter as st

usernames = pd.read_csv('Twitter Username Sample.csv', header = None).iloc[:,0]
for i in usernames:
    user = st.TwitterUser(i)
    print('My name is ' + user.get_twitter_name())
    print(user.get_twitter_bio())
    print('I have ' + user.get_twitter_follower() + ' followers.')
