#!/usr/bin/python
#-*- coding: utf-8 -*-
import tweepy

consumer_key = ""#access https://apps.twitter.com/ and get consumer key
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
print("Access this URL:" + auth.get_authorization_url())
verifier = raw_input('Verifier:')
auth.get_access_token(verifier)
print "Access Token:", auth.access_token
print "Access Token Secret:", auth.access_token_secret
