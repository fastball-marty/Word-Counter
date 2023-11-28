import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import csv

# Read the contents of 'pamela.txt'
with open('pamela.txt', 'r', encoding='utf-8') as file:
  text = file.read()

# Preprocess the text
def preprocess_text(text):
  sentences = nltk.sent_tokenize(text)

  #tokens = word_tokenize(text.lower())
  #filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
  #lemmatizer = WordNetLemmatizer()
  #lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
  #processed_text = ' '.join(lemmatized_tokens)
  #return processed_text
  return sentences

# Apply the preprocessing function
processed_text = preprocess_text(text)

# associate each sentence with a sentiment value, and store in a dictionary
def get_sentiment(processed_text):
  sentiments = dict()
  #scores = analyzer.polarity_scores(text)
  #sentiment = 1 if scores['pos'] > 0 else 0
  #return sentiment
  for sentence in processed_text:
    # Initialize NLTK sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    # determine sentiment strength
    ss = sid.polarity_scores(sentence)
    # add each sentence and its sentiment to dictionary 
    sentiments[sentence] = 1 if ss['pos'] > 0 else 0

  #return sum(sentiments) / len(sentiments)
  return sentiments

    
# Apply get_sentiment function
sentiments = get_sentiment(processed_text)

# Print the sentiments
# print(sentiments)

# convert a dictionary to csv
def convert_to_csv(dictionary):
  # Specify the file name
  csv_file = 'output.csv'

  # Writing the dictionary to a CSV file
  with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(['Text', 'Positive'])

    # Write key-value pairs
    for key, value in dictionary.items():
        writer.writerow([key, value])

# convert sentiment dictionary to csv
convert_to_csv(sentiments)


# print classification report
# print(classification_report(df['Positive'], df['sentiment']))

# print confusion matrix
# print(confusion_matrix(df['Positive'], df['sentiment']))