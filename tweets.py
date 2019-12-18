class Tweet:
    def __init__(self, idstr, screen_name, retweets):
        self.text = idstr
        self.user = screen_name
        self.rt = retweets

    def retweets(self):
        return self.rt

class ListTweet:
    def __init__(self, idstr, screen_name):
        self.text = idstr
        self.user = screen_name 
 
import sys
import tweepy
import codecs
from operator import methodcaller


consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""
# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth) 
outfile = "out.txt"
l =[Tweet('tweet.idstr', "user", 1)] 

lists =[ListTweet('dvar8r', "googledev"),ListTweet('mashable', "social-media"),ListTweet('Scobleizer', "ai-ml-and-data-science"),ListTweet('louisgray', "toptechbloggers"),ListTweet('Scobleizer', "tech-news")] 

oldest = -1

fp = codecs.open(outfile,"w","utf-8")


for listtweet in lists: 
    mentions = api.list_timeline(listtweet.text,listtweet.user, count=200) 
    for tweet in mentions: 
        if tweet.user.screen_name !='nsdevaraj': 
            twobj = Tweet(tweet.id_str, 
            tweet.user.screen_name, tweet.retweet_count) 
            l.append(twobj)
            oldest = tweet.id 

if oldest != -1:
    while True:   
        lsorted = sorted(l, key=methodcaller('retweets'), reverse=True) 
        for listitem in lsorted:
            if listitem.rt > 180: 
                fp.write('<div class="tweet" id="%s"></div> \n' % listitem.text )
        fp.write('</body></html>')
        fp.close()
        sys.exit()  
        
fp.close()
