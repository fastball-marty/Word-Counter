import re
import unicodedata

def word_count(fileName, filterStopWords):
  """
  This function stores the occurences of each word 
  in a dictionary sorted from most occuring word to least. 
  Boolean filterStopWords used to optionally filter 
  out common words.
  """
  # List of common filler words -- feel free to add/remove any
  stopwords = [
    'the', 'and', 'a', 'to', 'of', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for',
    'on', 'are', 'as', 'with', 'his', 'they', 'at', 'be', 'this', 'have', 'from',
    'or', 'one', 'had', 'by', 'but', 'not', 'what', 'all', 'were', 'we', 'when',
    'your', 'can', 'said', 'there', 'an', 'each', 'which', 'she', 'do', 'how',
    'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these',
    'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look',
    'two', 'more', 'go', 'see', 'no', 'way', 'could', 'people', 
    'than', 'first', 'been', 'who', 'its', 'now', 'find', 'long',
    'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part', 'me', 'am', 'shall', 'should',
    'very', 'upon', 'might', 'much', 'such', 'though', 'yet', 'too', 'any'
  ]

  try:
    # Read file
    file = open(fileName, 'r')
    content = file.read()
    file.close()
              
    # Clean text 
    words = basic_clean(content)
    words = words.split()

    # Count the occurrences of each word
    for word in words:
      word_count[word] = word_count.get(word, 0) + 1
      
    # Sort from most occuring word to least
    word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

    # Remove entries from word_count that exist in stopwords if selected
    if (filterStopWords):
      word_count = {word: count for word, count in word_count.items() if word.lower() not in stopwords}

    return word_count
  
  # Handle errors  
  except FileNotFoundError:
    print(f"File not found: {fileName}. Are wordcounter.py and your .txt file in the same directory?")
    return 
  except Exception as e:
    print(f"An error occurred: {e}")
    return

def format_output(dictionary, size):
  """
  This function takes a dictionary and formats it
  into a string where each key-value pair is on
  its own line. size paramater to limit dictionary 
  length, set to None if no limit.
  """
  # Check if the dictionary is empty
  if not dictionary:
    return 

  # Declare output string
  formatted_output = ""

  # If valid size
  if (size is not None) and (size < len(dictionary)):
    count = 0
    # Add size # of key-value pairs to string
    for key, value in dictionary.items():
      formatted_output += f"{key}: {value}\n"
      count += 1
      if (count == size):
        break
  # Else add all key-value pairs to string
  else: 
    for key, value in dictionary.items():
      formatted_output += f"{key}: {value}\n"

  return formatted_output
  
def compare_dictionaries(dict1, dict2):
  """
  This function takes two dictionaries, and 
  creates new lists to store keys not shared 
  between dictionaries.
  """
  unique_values_dict1 = [key for key in dict1.keys() if key not in dict2.keys()]
  unique_values_dict2 = [key for key in dict2.keys() if key not in dict1.keys()]

  return unique_values_dict1, unique_values_dict2

# This function is credited to https://github.com/m3redithw/data-science-visualizations/blob/main/WordClouds/prepare.py
# Original Author: Meredith Wang
# License: MIT License
# See clean.py for license
def basic_clean(string):
    '''
    This function takes in a string and
    returns the string normalized.
    '''
    string = unicodedata.normalize('NFKD', string)\
             .encode('ascii', 'ignore')\
             .decode('utf-8', 'ignore')
    string = re.sub(r'[^\w\s]', '', string).lower()
    return string


if __name__ == "__main__":
  """
  Main used to run program locally and count
  a custom .txt file. Results stored in output.txt
  in the same directory. 
  """
  # Prompt for name of file to read
  file_name = input("Please enter a file name. (The file must be a .txt, and the file must be in the same directory as myapp.py): ")

  while True:
    try:
      # Prompt for count all words or exclude common words
      option = int(input("Enter 0 to count all words or 1 to exclude common words: "))

      # Ensure the entered option is either 0 or 1 & save selection
      if option == 0:
        includeCommonWords = False
        break
      elif option == 1:
        includeCommonWords = True
        break
      else:
          print("Please enter either 0 or 1.")

    except ValueError:
      print("Invalid input. Please enter a number.")

  # Write output to file if exists
  with open('output.txt', 'w') as file:
    wc = word_count(file_name, includeCommonWords)
    if (wc is not None):
      file.write(format_output(wc, None))
      print("Success! See output.txt for results.")
    else:
      print("Error in program. See above messages.")