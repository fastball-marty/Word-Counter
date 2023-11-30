import os
import csv
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Preprocess the text
def preprocess_text(text):
  # cut token off at '.', '!', '?', ';', or ':'
  custom_pattern = r'\w.*?[.!?;:]'

  # replace apostrophe unicode
  text = text.replace("’", "'")

  tokenizer = RegexpTokenizer(custom_pattern)

  sentences = tokenizer.tokenize(text)

  return sentences


# associate each token with a sentiment value, and store in a dictionary
def get_sentiment(processed_text):
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


# convert a dictionary to csv
def convert_to_csv(dictionary):
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

# find sentences w/highest negative values and highest positive values
def max_and_mins(dictionary):
  top_5_neg = sorted(dictionary.items(), key=lambda x: x[1]['neg'], reverse=True)[:5]
  print(len(top_5_neg))

  top_5_pos = sorted(dictionary.items(), key=lambda x: x[1]['pos'], reverse=True)[:5]
  print(len(top_5_pos))

  for item, values in top_5_neg:
    print(f"{item}: {values}")

  for item, values in top_5_pos:
    print(f"{item}: {values}")


if __name__ == '__main__':

  # get abs path of this file
  script_directory = os.path.dirname(os.path.abspath(__file__))
  # add path to pamela
  file_path = os.path.join(script_directory, '..', 'assets', 'pamela.txt')

  # read file if path exists
  if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
      text = file.read()
  else:
    print(f"The file {file_path} does not exist.")

  processed_text = preprocess_text(text)
  sentiments = get_sentiment(processed_text)
  max_and_mins(sentiments)
  #convert_to_csv(sentiments)