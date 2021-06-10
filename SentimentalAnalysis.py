from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt

#function to calculate percentage
def percentage(part,whole):
    return 100* float(part)/float(whole)

#entering consumers details
consumerKey="Fv6eTDS1N6rEaCWhdDDcEZpIo"
consumerSecret="wRVBmyNcSPfW4j1hb3cllYuisJBZoAljJ1K02b0Ss5hBqOgSvW"
accessToken="1102164287433302017-2b6qqjDbDBwABPp6XrswM6x4MQGnqz"
accessTokenSecret="MwKdMvoPwOGUoobqR47ZGwQELgrddQGZ6aemQrnThMHa9"

#creating connection with twitter
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

#inputing the terms to be searched
searchTerm = input("Enter keyword/hashtag to search about : ")
noOfSearchTerms = int(input("Enter how many tweets to analyze : "))

tweets = tweepy.Cursor(api.search , q=searchTerm).items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
   # print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

#calculating whether a tweet is positive,negative or neutral
    if(analysis.sentiment.polarity == 0):
        neutral +=1
    elif(analysis.sentiment.polarity < 0.00):
        negative +=1
    elif(analysis.sentiment.polarity > 0):
        positive +=1

positive = percentage(positive , noOfSearchTerms)
negative = percentage(negative , noOfSearchTerms)
neutral = percentage(neutral , noOfSearchTerms)
polarity = percentage(polarity , noOfSearchTerms)

positive=format(positive,'.2f')
neutral=format(neutral,'.2f')
negative=format(negative,'.2f')

print("How people are reacting on "+ searchTerm + " by analyzing " + str(noOfSearchTerms) + " Tweets.")
if(polarity==0):
    print("Neutral")
elif(polarity<0.00):
    print("Negative")
elif(polarity>0.00):
    print("Positive")

#additional python libraries
labels = ['Positive ['+str(positive)+'%]','Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]'] 
sizes=[positive,neutral,negative]
colors=['yellowgreen','gold','red']
patches,texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on '+searchTerm+' by analyzing '+str(noOfSearchTerms)+' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
