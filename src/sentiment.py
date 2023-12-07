import os
import csv
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer

def preprocess_text(fileName):
  """
  This function takes a file of text and
  splits it into its individual sentences
  based off a custom regex pattern.
  """
   # Read file
  file = open(fileName, "r")
  text = file.read()
  file.close()

  # cut token off at '.', '!', '?', ';', or ':'
  custom_pattern = r'\w.*?[.!?;:]'

  # replace apostrophe unicode
  text = text.replace("’", "'")

  tokenizer = RegexpTokenizer(custom_pattern)

  sentences = tokenizer.tokenize(text)

  return sentences

def get_sentiment(processed_text):
  """
  This function associates each token with a sentiment value,
  and stores that token/sentiment key-value pair in a dictionary.
  """

  sentiments = dict()

  for sentence in processed_text:
    # Initialize NLTK sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    # determine sentiment strength
    ss = sid.polarity_scores(sentence)
    # add each sentence and its sentiment to dictionary 
    # sentiments[sentence] = 1 if ss['pos'] > ss['neg'] else 0
    sentiments[sentence] = ss
    
  return sentiments

def convert_to_csv(dictionary):
  """
  This function takes a dictionary and converts
  it to a csv.
  """
  # Specify the file name
  csv_file = 'output.csv'

  # write to a CSV file
  with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # header
    writer.writerow(['Text', 'Positive'])
    # each key-value pair as a row
    for key, value in dictionary.items():
        writer.writerow([key, value])

def max_and_mins(dictionary):
  """
  This function takes a dictionary and finds the sentences with the 
  highest negative and the highest positive sentiments. Only the first
  15 for each sentiment are stored. The results are outputted to
  a formatted string.
  """
  top_15_neg = sorted(dictionary.items(), key=lambda x: x[1]['neg'], reverse=True)[:15]

  top_15_pos = sorted(dictionary.items(), key=lambda x: x[1]['pos'], reverse=True)[:15]

  output = ""

  output += "Highest Negative Sentiments: \n"

  for item, values in top_15_neg:
    output+= (f"{item}: {values}\n")

  output += "\n"  

  output += "Highest Positive Sentiments: \n"

  for item, values in top_15_pos:
    output += (f"{item}: {values}\n")

  return output

def sentiment_analysis(fileName):
  """
  This function combines the above methods (excluding
  convert_to_csv) to perform sentiment analysis on a
  file.
  """
  return max_and_mins(get_sentiment(preprocess_text(fileName)))

def average_sentiment(dictionary):
  """
  This function takes a dictionary of sentiments and computes
  its average pos, neg, neu, compound values.
  """

  # Initialize variables to store cumulative sums
  total_pos, total_neg, total_neu, total_compound = 0, 0, 0, 0
  num_entries = len(dictionary)

  # Calculate cumulative sums
  for values_dict in dictionary.values():
    total_pos += values_dict.get('pos', 0)
    total_neg += values_dict.get('neg', 0)
    total_neu += values_dict.get('neu', 0)
    total_compound += values_dict.get('compound', 0)

  # Calculate averages
  avg_pos = round(total_pos / num_entries, 4)
  avg_neg = round(total_neg / num_entries, 4)
  avg_neu = round(total_neu / num_entries, 4)
  avg_compound = round(total_compound / num_entries, 4)
  
  # Create and return the result dictionary
  result_dict = {'avg_pos': avg_pos, 'avg_neg': avg_neg, 'avg_neu': avg_neu, 'avg_compound': avg_compound}
  return result_dict