# Twitter Lists Curation

Fork this repository and fill these details from your https://developer.twitter.com/en/apps


https://github.com/nsdevaraj/tweets/blob/master/tweets.py#L21

consumer_key=""

consumer_secret=""

access_token=""

access_token_secret=""


Do execute :
pip install tweepy

Modify the line below for your favorite twitter lists:
https://github.com/nsdevaraj/tweets/blob/master/tweets.py#L36

For sorting based on "likes" instead of "retweets", modify below line to:
  tweet.user.screen_name, tweet.favorite_count) 

https://github.com/nsdevaraj/tweets/blob/master/tweets.py#L48

Modify the limit by editing the below line:
https://github.com/nsdevaraj/tweets/blob/master/tweets.py#L56

Follow steps for Github Pages:
https://help.github.com/en/enterprise/2.13/user/articles/configuring-a-publishing-source-for-github-pages

Now your project is ready, execute "fetch.sh"

It will update your published github page with latest fetched tweets

Edit git config as below to store your repository with credentials (not recommended)
https://username:pass%40word@github.com/myRepoDir/myRepo.git

I do use https://github.com/termux/termux-widget with alias to fetch.sh stored in $HOME/.shortcuts/ of my android
