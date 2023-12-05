# regular expression import
import re

# uni-code library
import unicodedata


# basic_clean provided by @m3redithw
# see prepare.py for more info
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

def word_count(fileName):
  """
  This function takes a txt file and cleans the text,
  then counts the occurences of each word and sorts
  from most common to least.
  """
  # Declare dictionary
  word_count = {}

  try:
    # Read file
    file = open(fileName, "r")
    content = file.read()
    file.close()
              
    # Clean text 
    words = basic_clean(content)

    # Split into list
    words = words.split()

    # Count the occurrences of each word
    for word in words:
      word_count[word] = word_count.get(word, 0) + 1
      
    # Sort from most occuring word to least
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

    return sorted_word_count

  # Handle exceptions
  except FileNotFoundError:
    print(f"Error: The file '{fileName}' does not exist. Is the file located in the same directory as wordcounter.py?")
  except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")

def filtered_word_count(fileName):
  """
  This function takes a txt file and cleans the text,
  then counts the occurences of each word and sorts
  from most common to least. This function ignores common
  filler words.
  """
  # List of common filler words -- feel free to add/remove any
  common_function_words = [
    'the', 'and', 'a', 'to', 'of', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for',
    'on', 'are', 'as', 'with', 'his', 'they', 'at', 'be', 'this', 'have', 'from',
    'or', 'one', 'had', 'by', 'word', 'but', 'not', 'what', 'all', 'were', 'we', 'when',
    'your', 'can', 'said', 'there', 'use', 'an', 'each', 'which', 'she', 'do', 'how',
    'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these',
    'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look',
    'two', 'more', 'write', 'go', 'see', 'number', 'no', 'way', 'could', 'people', 'my',
    'than', 'first', 'water', 'been', 'call', 'who', 'oil', 'its', 'now', 'find', 'long',
    'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part', 'me', 'am', 'shall', 'should',
    'very', 'upon', 'might', 'much', 'such', 'though', 'yet', 'too', 'any'
  ]

  # Declare dictionaries
  word_count = {}
  filtered_word_count = {}

  try:
    # Read file
    file = open(fileName, "r")
    content = file.read()
    file.close()
              
    # Clean text 
    words = basic_clean(content)

    # Split into list
    words = words.split()

    # Count the occurrences of each word
    for word in words:
      word_count[word] = word_count.get(word, 0) + 1

    # Sort from most occuring word to lowest
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

    # Remove entries from word_count that exist in common_words
    filtered_word_count = {word: count for word, count in sorted_word_count.items() if word.lower() not in common_function_words}

    return filtered_word_count

  # Handle exceptions
  except FileNotFoundError:
    print(f"Error: The file '{fileName}' does not exist. Is the file located in the same directory as wordcounter.py?")
  except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")

def format_output(dictionary):
  """
  This function takes a dictionary and formats it
  into a string where each key-value pair is on
  its own line.
  """
  # Check if the dictionary is empty
  if not dictionary:
    return 

  # Declare output string
  formatted_output = ""

  # Add key-value pairs to string
  for key, value in dictionary.items():
    formatted_output += f"{key}: {value}\n"

  return formatted_output


def limit_format_output(dictionary):
  """
  This function takes a dictionary and formats it
  into a string where each key-value pair is on
  its own line. Only displays the first 100 entries
  of the dictionary.
  """
  # Check if the dictionary is empty
  if not dictionary:
    return 
  
  # Declare output string
  formatted_output = ""

  # Count to 100 
  count = 0

  # Add key-value pairs to string
  for key, value in dictionary.items():
    formatted_output += f"{key}: {value}\n"
    count +=1

    if (count == 100):
      break

  return formatted_output

def compare_dictionaries(dict1, dict2):
  """
  This function takes two dictionaries, and 
  creates new lists to store keys not shared 
  between dictionaries.
  """
  # Get the unique values from each dictionary
  unique_values_dict1 = [key for key in dict1.keys() if key not in dict2.keys()]
  unique_values_dict2 = [key for key in dict2.keys() if key not in dict1.keys()]

  return unique_values_dict1, unique_values_dict2



# Main to run program locally with custom file
if __name__ == "__main__":
  # Get .txt file name
  file_name = input("Please enter a file name. (The file must be a .txt, and the file must be in the same directory as myapp.py): ")

  while True:
    try:
      # Ask the user for the word count option
      option = int(input("Enter 0 to count all words or 1 to exclude common words: "))

      # Check if the entered option is either 0 or 1
      if option in [0, 1]:
          break
      else:
          print("Please enter either 0 or 1.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  # include filler words
  if option == 0:
    print (format_output(word_count(file_name)))
  
  # ignore filler words
  else:
    print (format_output(filtered_word_count(file_name)))