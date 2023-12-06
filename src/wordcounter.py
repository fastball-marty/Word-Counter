# see clean.py
import clean

def word_count(fileName, filterStopWords):
  """
  This function takes a txt file and normalizes the text,
  then counts the occurences of each word and sorts
  from most common to least. Boolean filterStopWords used
  to optionally filter out common words.
  """
  # Declare dictionary
  word_count = {}

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
    file = open(fileName, "r")
    content = file.read()
    file.close()
              
    # Clean text, 
    words = clean.basic_clean(content)

    # Split into list
    words = words.split()

    # Count the occurrences of each word
    for word in words:
      word_count[word] = word_count.get(word, 0) + 1
      
    # Sort from most occuring word to least
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

    # If chose to filter stopwords,
    if (filterStopWords):
      # Remove entries from word_count that exist in stopwords
      sorted_word_count = {word: count for word, count in sorted_word_count.items() if word.lower() not in stopwords}

    return sorted_word_count

  # Handle exceptions
  except FileNotFoundError:
    print(f"Error: The file '{fileName}' does not exist. Is the file located in the same directory as wordcounter.py?")
  except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")

def format_output(dictionary, size):
  """
  This function takes a dictionary and formats it
  into a string where each key-value pair is on
  its own line. size optional paramater to
  limit dictionary to certain length.
  """
  # Check if the dictionary is empty
  if not dictionary:
    return 

  # Declare output string
  formatted_output = ""

  # If size exists, and size < length of dictionnary
  if (size) and (size < len(dictionary)):
    count = 0
    # Add size # of key-value pairs to string
    for key, value in dictionary.items():
      formatted_output += f"{key}: {value}\n"
      count += 1

      if (count == size):
        break

  else: 
    # Add all key-value pairs to string
    for key, value in dictionary.items():
      formatted_output += f"{key}: {value}\n"

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
    # Open a file for writing (creates the file if it doesn't exist)
    with open('output.txt', 'w') as file:
      # Write content to the file
      file.write(format_output(word_count(file_name, False), None))

  # ignore filler words
  else:
    # Open a file for writing (creates the file if it doesn't exist)
    with open('output.txt', 'w') as file:
      # Write content to the file
      file.write(format_output(word_count(file_name, True), None))