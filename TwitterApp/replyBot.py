#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tweepy
import datetime

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += datetime.timedelta(hours=9)
        
        #favo when reply
        if str(status.in_reply_to_screen_name)==Twitter_ID and str(status.user.screen_name)!=Twitter_ID:
            print(str(datetime.datetime.today()))
            api.create_favorite(status.id)
        #            tweet = "@" + str(status.user.screen_name) + " " + "Hello！\n" + str(datetime.datetime.today())
        #            api.update_status(status=tweet)
        return True
    
    def on_error(self, status_code):
        print('Error code:' + str(status_code))
        return True
    
    def on_timeout(self):
        print('Timeout error')
        return True



consumer_key = ""#access https://apps.twitter.com/ and get consumer key
consumer_secret = ""
access_token = ""
Twitter_ID = ""#Your TwitterID(Don't need @)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.userstream()
