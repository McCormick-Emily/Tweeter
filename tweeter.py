import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
import csv
import numpy as np

class Tweetter:

  ## define constructor
  def __init__(self, sterms):
    ## Setting instance variables
    self.search_terms = sterms #instance var: set via object creation
    self.tweets = []           #class var: set in constructor
    self.good_words = []
    self.bad_words = []
  
  ## @params: Search terms
  ## @return: Array of Strings (just messages)
  def query_twitter(self):
    ## Setting a limit of tweets to the array. 
    ## Using a function to pass arguments as the search terms(query).
    limit = 100
    query = self.search_terms 

    ## Scraping the twitter API to collect the data, but specifically asking for just the tweet content. 
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
      if len(self.tweets) == limit:
        break
      else:
          self.tweets.append(tweet.rawContent)

  ## Changing the format in the csv files to extract just the words from both the positive and negative csv files.
  def csv_files(self):
    positive_words = pd.read_csv('../../Downloads/positivewords.csv', encoding = "utf-8")
    positive_words.columns = ["number", "word"]
    df = pd.DataFrame(positive_words, columns = ["word"])
    p = df.to_numpy()
    for i in range(len(p)):
      self.good_words.append(p[i][0]) ##Access 2d array
    print(self.good_words[1])

    negative_words = pd.read_csv('../../Downloads/negativewords.csv', encoding = "ISO-8859-1")
    negative_words.columns = ["number", "word"]
    df = pd.DataFrame(negative_words, columns = ["word"])
    n = df.to_numpy()
    for i in range(len(n)):
      self.bad_words.append(n[i][0])
    print(self.bad_words[1])

  def comparison(self):
    ## Creating a for loop that takes the length of the tweets and formats them to a more comparable state. 
    ## By changing the synatx and creating spaces inbetween the words.
    tweet_sz = len(self.tweets)
    for t in range(tweet_sz):
      counter_good = 0
      counter_bad = 0   
      good_words_found = []
      bad_words_found = []
      string = self.tweets[t]
      string = string.lower()
      word_array = string.split(" ")
      print('\n')
      print("THE TWEET: ")          
      print(string)
      ## Set a counter to count score of the good and bad words in the overall tweet.
      ## Nested for loops are comparing the word in the tweet array to the word in the csv files array.
      ## The for loop is also storing the compared word into a separate array. 
      for word in word_array:
        for good in self.good_words:
          if word.find(good) == 0:
            good_words_found.append(word)
            counter_good = counter_good + 1

        for bad in self.bad_words:
          if word.find(bad) == 0:
            bad_words_found.append(word)
            counter_bad = counter_bad + 1 

      self.print_results(counter_good, counter_bad, good_words_found, bad_words_found) 
      ## Calling the method print_results after the word comparison for each individual tweet.
  
  def print_results(self, counter_good, counter_bad, good_words_found, bad_words_found):
    print('\n')
    print('Score Board For Tweet:')
    print(f'Good Score:  {counter_good}')
    print(f'Bad Score:   {counter_bad}')
    
    ## Creating the score board based off the counters set in the comparison function. 
    if counter_bad > counter_good:
      print("This Tweet Was Overall Bad")
    else:
      print("This Tweet Was Overall Good")
    print(f'Good Words Found: {good_words_found}')
    print(f'Bad Words Found: {bad_words_found}') 

## Setting the instance variable to a specific query seach term in the constructor.
kard = Tweetter("khloe kardashian + tristain + cheat")
hotd = Tweetter("hotd + dragon +targaryen")
bach = Tweetter("bachelor in paradise + mexico + crying")

## Calling each function.

kard.query_twitter()
kard.csv_files()
kard.comparison()

hotd.query_twitter()
hotd.csv_files()
hotd.comparison()

bach.query_twitter()
bach.csv_files()
bach.comparison()