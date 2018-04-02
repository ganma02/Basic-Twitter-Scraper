# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:37:22 2018
Twitter Scraper
@author: win_8
"""

import requests
import bs4

class TwitterUser():
    
      def __init__(self, username):
          self.username = username
            
      # Getting twitter name by using username
      def get_twitter_name(self):
          res = requests.get('https://twitter.com/{}'.format(self.username))
          #res.raise_for_status()
      
          twitterSoup = bs4.BeautifulSoup(res.text, 'lxml')
          a_search = twitterSoup.select('a')
          
          # Finding the index of 'a' that has the name
          for a,b in enumerate(a_search):
                if a_search[a].get('href') == '/' + self.username:
                    return a_search[a].getText().strip()
      
      # Getting twitter bio by using username
      def get_twitter_bio(self):
          res = requests.get('https://twitter.com/{}'.format(self.username))
          #res.raise_for_status()
          
          # Finding the bio using HTML 'p' 
          twitterSoup = bs4.BeautifulSoup(res.text, 'lxml')
          p_search = twitterSoup.select('p')
          return p_search[0].getText()
      
      
      # Getting amount of followers in twitter by using username
      def get_twitter_follower(self):
          res = requests.get('https://twitter.com/{}'.format(self.username))
          #res.raise_for_status()
      
          twitterSoup = bs4.BeautifulSoup(res.text, 'lxml')
          span_search = twitterSoup.select('span')
          
          # Finding the index of 'span' that has the followers count
          for a,b in enumerate(span_search):
                if span_search[a].getText() == 'Follower':
                      return str(span_search[a + 2].getText())

#if __name__ == '__main__':
    # user = TwitterUser('testuser')
    # print('My name is ' + user.get_twitter_name())
    # print(user.get_twitter_bio())
    # print('I have ' + user.get_twitter_follower() + ' followers.')