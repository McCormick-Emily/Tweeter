import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
import csv
import numpy as np


query = "khloe kardashian + tristain + cheat"
tweets = []
limit = 100
good_words = []
bad_words = []
#good_array = ["dating", "love", "peace", "kissed", "family", "friends"]
#bad_array = ["cheat", "scandal", "fuck", "thatwhitegirl"]

# This is the csv file for good & bad words

positive_words = pd.read_csv('../../Downloads/positivewords.csv', encoding = "utf-8")
#print(positive_words)
negative_words = pd.read_csv('../../Downloads/negativewords.csv', encoding = "ISO-8859-1")
#print(negative_words)

# Positive words: Changing the format to be just the word in the array.

data = pd.read_csv('../../Downloads/positivewords.csv', encoding = "utf-8")
data.columns = ["number", "word"]
df = pd.DataFrame(data, columns = ["word"])
#print(data.columns)
#print(df.columns[:1])
#print(df.to_numpy())
p = df.to_numpy()
#print(e[0][0])

# For loop indicating the exact spot in the array; storing that data in another array to compare data.
for i in range(len(p)):
	good_words.append(p[i][0])
print(good_words[1])




# Negative words: Changing the format to be just the word in the array.

data1 = pd.read_csv('../../Downloads/negativewords.csv', encoding = "ISO-8859-1")
data1.columns = ["number", "word"]
df = pd.DataFrame(data1, columns = ["word"])
#print(data1.columns)
#print(df.columns[:1])
#print(df.to_numpy())
n = df.to_numpy()
# print(f)
# print(f[0][0])
# print(f[1][0])
# print(f[3][0])

for i in range(len(n)):
	bad_words.append(n[i][0])
print(bad_words[1])



for tweet in sntwitter.TwitterSearchScraper(query).get_items():
#	print(vars(tweet))
#	break	
	if len(tweets) == limit:
		break
	else:
		tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns =['Date','user','Tweet'])
print(df)
tweet_sz = len(tweets) 	# get length of tweets
						# get message
#print(tweet_sz)
	

	#compare					# for t in range(len(tweets)):
for t in range(tweet_sz):
	counter_good = 0
	counter_bad = 0		# print(tweets[t]) #(date, author, msg)
						# msg_sz = tweets[t]
						# print(tweets[t][2])
	string = tweets[t][2]
	string = string.lower()
	word_array = string.split(" ")
	#print(word_array)
	
	print('\n')
	print("THE TWEET: ")					# print("start")
	print(string)
						# print(good_array[0])
						# print(string.find(good_array[0]))
#compare
	for word in word_array:
		for good in good_words:
			#print(word)
			#print(" From good array: " + good)
			if word.find(good) >= 0:
										# if good == word:
										# print(word)
				counter_good = counter_good + 1						# print(good)
				#print(string + " :Found positive words")
		for bad in bad_words:
			#print(word)
			#print(" From bad array: " + bad)
			if word.find(bad) >= 0:
										#print(word)
										#print(bad)
										#print(string)
				#print(string + " :Found negative words")
				counter_bad = counter_bad + 1
				#print(counter_bad)
				#print("bad")

	print('\n')
	print('Score Board for Tweet:')
	print(f'Good score:  {counter_good}')
	print(f'Bad Score:   {counter_bad}')

	if counter_bad > counter_good:
		#counter_bad = counter_bad + 1
		print("This Tweet was overall bad")
	else:
		#counter_good = counter_good + 1
		print("This Tweet was overall good")
	# print('\n')
	# print('Score Board for Tweet:')
	# print(f'Good score:  {counter_good}')
	# print(f'Bad Score:   {counter_bad}')



































#if bad == word:
#print("em")
# for tweet in tweets:
# 	print("yes")
# 	print(tweet)
# 	print(tweet[2]) #kylie sucks
	
# 	#for loop for just good words
# 		#print(goodWord)
# 		#print(tweet[2])
# 	#for loop for just bad words

# 	for rcv in (good, bad):
# 		print("cool")
# 		print(rcv)

# 		if tweet == good: #string methods indexOf
# 			print("this is good")
# 		elif tweet == bad:
# 			print("this is bad")
#	break 
# if tweets == "dating":
# 	print("happy")
# else:
# 	print("sad")














# # Setting variables to be used in format string command below
# tweet_count = 100
# username = "jack"

# # Using OS library to call CLI commands in Python
# os.system("snscrape --jsonl --max-results {} twitter-search 'from:{}'> user-tweets.json".format(tweet_count, username))

# # Reads the json generated from the CLI command above and creates a pandas dataframe
# tweets_df1 = pd.read_json('user-tweets.json', lines=True)

# # Displays first 5 entries from dataframe
# print(tweets_df1.head())