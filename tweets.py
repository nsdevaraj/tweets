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


def write_tweet(text):  
    api.update_status(status=text)

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

# get list of users by 100 +list

#api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#lst = [
#        283051440,
#        277452100,
#        705431391706681344,
#        .....
#        885435593953619969,
#        706025541531357184]
#def chunks(lst, n):
#    """Yield successive n-sized chunks from lst."""
#    for i in range(0, len(lst), n):
#        yield lst[i:i + n]
#        
#x100x = [lst[i:i + 100] for i in range(0, len(lst), 100)]

#dic = {}
#for ids in x100x:
#    user_objs = api.lookup_users(user_ids=ids)
#    list_of_followers = []
#    for user in user_objs:
#        list_of_followers.extend(user.screen_name)
	
	
#dic['screen_name'] = list_of_followers
#outFile = open('Followers.txt','w')
#json.dump(dic,outFile,indent=4)