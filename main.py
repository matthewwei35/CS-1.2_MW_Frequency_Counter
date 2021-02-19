from HashTable import HashTable
from os import path
import string
# from TesterFunction import test_counter



print('''Welcome to Word Frequency Counter! 📊 

This program will:
- Count the number of occurrences of each word in the file.
- Print all of the words and their frequencies.
_______________________________________________________
''')



# Prompts the user to enter the name of a .txt file
# For testing, enter example.txt

filename = input("📝  What is the name of the .txt file? ")

# Continues to prompt the user until an existing file is entered.
while path.exists(filename) == False:
  print(f"\nThe file named {filename} does not exist in this directory. Try again. \n")
  filename = input("🔁  What is the name of the .txt file? ")



# Creates a list of every word from the txt file without
# spaces and punctuation. It also lowercases the words.

words_in_file = []
with open(filename,'r') as file: 
  for line in file: 
    for word in line.split(): 
      word = word.strip(string.punctuation)
      words_in_file.append(word.lower())
      



# Prints message to user stating how many words are being added to the table.
# Also displays the list of words that wre generated above.

print(f'''

✅  We found the following {len(words_in_file)} words in {filename}:

{words_in_file}


⬇️  Now adding {len(words_in_file)} words from {filename} to the Frequency Counter...

''')


# Instatiates a Hash Table object with size 8
# called word_frequency

frequency_counter = HashTable(8)


# Iteratives over  words_in_file list and adds each word in to the Hash Table one word at a time (using Chaining for collision)


for word in words_in_file:
  frequency_counter.insert(word, 1)


print(f"🖨  All done! Here are all of the words from {filename} and their frequencies:\n")


frequency_counter.print_key_values()



# THIS IS TO ONLY BE USED FOR TESTING. THIS IS NOT A SOLUTION.
# test_counter(words_in_file)