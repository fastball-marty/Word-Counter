class MyApp:

  @staticmethod
  def word_count(fileName):
    word_count = {}

    try:
      file = open(fileName, "r")
    
      content = file.read()

      file.close()
                
      # Tokenize the content into words
      words = content.split()

      # Count the occurrences of each word
      for word in words:
        # Remove punctuation and convert to lowercase for better counting accuracy
        cleaned_word = word.strip(".,!;:?()[]—{}\"'").lower()

        # Update the word count in the dictionary
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    except FileNotFoundError:
      print(f"Error: The file '{fileName}' does not exist. Is the file located in the same directory as myapp.py?")
    except PermissionError:
      print(f"Error: Permission denied to open the file '{fileName}'.")
    except IOError as e:
      print(f"Error: An I/O error occurred while opening the file '{fileName}': {e}")
    except Exception as e:
      print(f"Error: An unexpected error occurred: {e}")

    # sort from most occuring word to lowest
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

    return sorted_word_count


  @staticmethod
  def filtered_word_count(fileName):
    common_function_words = [
      'the', 'and', 'a', 'to', 'of', 'in', 'is', 'you', 'that', 'it', 'he', 'was', 'for',
      'on', 'are', 'as', 'with', 'his', 'they', 'i', 'at', 'be', 'this', 'have', 'from',
      'or', 'one', 'had', 'by', 'word', 'but', 'not', 'what', 'all', 'were', 'we', 'when',
      'your', 'can', 'said', 'there', 'use', 'an', 'each', 'which', 'she', 'do', 'how',
      'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these',
      'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look',
      'two', 'more', 'write', 'go', 'see', 'number', 'no', 'way', 'could', 'people', 'my',
      'than', 'first', 'water', 'been', 'call', 'who', 'oil', 'its', 'now', 'find', 'long',
      'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part', 'me', 'am', 'shall', 'should'
    ]

    word_count = {}
    filtered_word_count = {}

    try:
      file = open(fileName, "r")
    
      content = file.read()

      file.close()
                
      # Tokenize the content into words
      words = content.split()

      # Count the occurrences of each word
      for word in words:
        # Remove punctuation and convert to lowercase for better counting accuracy
        cleaned_word = word.strip(".,!;:?()[]{}\"'").lower()

        # Update the word count in the dictionary
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

      # sort from most occuring word to lowest
      sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

      # remove entries from word_count that exist in common_words
      filtered_word_count = {word: count for word, count in sorted_word_count.items() if word.lower() not in common_function_words}

    except FileNotFoundError:
      print(f"Error: The file '{fileName}' does not exist. Is the file located in the same directory as myapp.py?")
    except PermissionError:
      print(f"Error: Permission denied to open the file '{fileName}'.")
    except IOError as e:
      print(f"Error: An I/O error occurred while opening the file '{fileName}': {e}")
    except Exception as e:
      print(f"Error: An unexpected error occurred: {e}")

    return filtered_word_count

  @staticmethod
  def format_output(dictionary):
    formatted_output = ""
    for key, value in dictionary.items():
      formatted_output += f"{key}: {value}\n"

    return formatted_output


# main to run program locally with custom file
if __name__ == "__main__":

  my_app = MyApp()

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

  if option == 0:
    print (my_app.format_output(my_app.word_count(file_name)))
  else:
    print (my_app.format_output(my_app.filtered_word_count(file_name)))


