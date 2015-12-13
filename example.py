import tweepy

auth = tweepy.OAuthHandler("1pzPN2l5AdZPrHij0Rg59XFTx", "foPPIKpGDdUnjrmwcCNmtMZ4JExWmlZaWl3mWSFu4EnLZMqVPB")
auth.set_access_token("163954792-q255pAwFlpYji9JV2mFvWxnqNL4PJIDf6dnCOIj0", "vkICy3x0IFXn11RQhucHk71o6LCsdve7FmRImVrf3ADuI")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text