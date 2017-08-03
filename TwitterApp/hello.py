#!/usr/bin/python
#-*- coding: utf-8 -*-
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

api.update_status('Hello, world!')
