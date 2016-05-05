# Thomas Dobbs, 3-Headed Politician, (2016), bernie clintrump, https://github.com/TomDobbs/3Headed_Politician
import tweepy, time
from chain_builder import get_sentence
import cPickle as pickle
from datetime import timedelta
from keys import keys
from datetime import date, timedelta

# PULL TODAYS DATE
today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(1)

# ******************************************************
# Create Keys.py file and pull your API credentials to
# access Twitter's API.
# ******************************************************
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# PICKLE IN DICTIONARIES
with open('Pickles/forward_dict.pkl') as f:
    f_dict = pickle.load(f)

with open('Pickles/reversed_dict.pkl') as f:
    r_dict = pickle.load(f)

# INITIATE LIST TO HOLD TWEETS
tweet_replies = []

# ******************************************************
# Queries Popular Tweets directed at Candidates or using
# well-known Hashtags and responds to all queried tweets.
# ******************************************************
hashtags = ["#FeelTheBern OR #ImWithHer OR #MakeAmericaGreatAgain OR #Trump2016 \
OR @BernieSanders OR @HillaryClinton OR @realDonaldTrump"]

top_tweets = tweepy.Cursor(api.search, q=hashtags, count=100, result_type='popular', include_entities=True, monitor_rate_limit=True, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, lang="en", since=yesterday, until=today).items()

for status in top_tweets:
    if status.favorite_count > 1500:
        tweet_replies.append(status)

# ***************************************************
# Queries Tweets directed at or in reply to
# FeelTheBern_Bot and responds to all queried tweets.
# ***************************************************
bernbot_query = "to:FeelTheBern_Bot OR @FeelTheBern_Bot"

bernbot_tweets = tweepy.Cursor(api.search, q=bernbot_query, count=100, result_type='recent', include_entities=True, monitor_rate_limit=True, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, lang="en" since=yesterday, until=today).items()

for status in bernbot_tweets:
    tweet_replies.append(status)

# ************************************************
# Queries Tweets from Presidential Candidates and
# responds to those with greater than 500 likes.
# ************************************************
candidate_query = "from:BernieSanders OR from:HillaryClinton OR from:realDonaldTrump"

candidate_tweets = tweepy.Cursor(api.search, q=candidate_query, count=100, result_type='recent', include_entities=True, monitor_rate_limit=True, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, lang="en", since=yesterday, until=today).items()

for status in candidate_tweets:
    if status.favorite_count > 1500:
        tweet_replies.append(status)


# DROPS ANY DUPLICATE TWEETS SO IT DOES NOT RESPOND TWICE
tweet_replies = set(tweet_replies)

# BUILDS RESPONSES TO TWEETS AND REPLIES TO TWITTER ACCOUNTS
for tweet in tweet_replies:
    resp_length = 141
    user = tweet.user.screen_name
    text = tweet.text
    response = 'Vote trump 2016 Macy'
    n = 0
    while (resp_length > 140 or 'Vote trump 2016' in response or 'Macy' in response) and n < 20:
        response = get_sentence(text, f_dict, r_dict, randomness = 1)
        response = "@{0} {1}".format(user, response)
        resp_length = len(response)
        n += 1
    if 'Vote trump 2016' in response or 'Macy' in response or resp_length > 140:
        pass
    else:
        s = api.update_status(response, tweet.id)
        # UNHASH IF YOU WANT TWEETS SEPARTED BY 5 minutes
        time.sleep(300)
