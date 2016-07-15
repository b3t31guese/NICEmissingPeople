from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['@urgencesnice']) # let's define all words we would like to have a look for
    #tso.set_language('en', ) # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = '',
        consumer_secret = '',
        access_token = '',
        access_token_secret = ''
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        check=tweet['text']
        check.split()
        temp=0
        for a in check:
            if a=='RT':
                temp+=1
        if temp>=1:
            print 'retweet'
        else:
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
