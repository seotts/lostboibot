import tweepy

CONSUMER_KEY = 'Wp0oggGt5yrqEskmq0Deqb8hd'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'oh3DqtzKXJTSCrx3cEinoOVBs1F23OxtNJ62QC9WO68Z6Ih7I7'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3262706076-wdw5x6HWmPrPtlrmkNuL3eibiG3md4F1jEwmpqi'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'KFOB1GROLlc1sOC6b7AhONcoOzSWjJSr0mJnp1M750u0x'#keep the quotes, replace this with your access token secretauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(status=  "This is a test!!!" )
