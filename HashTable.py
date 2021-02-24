from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    """Creates an array of a given size that populates its elements with a LinkedList object."""
    counter = 0
    self.arr = []
    while counter < size:
      self.arr.append(LinkedList())
      counter += 1
    
    return self.arr

  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    """Returns an index value based on the key, which decides where in our list to put the key:value pair."""
    length = len(key)
    last_letter = key[length -1].lower()
    difference_from_z = ord('z') - ord(last_letter)
    index = difference_from_z % self.size
    
    return index

  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    pass


  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    # Use print_nodes but format to fit our case
    pass

if __name__ == "__main__":

  ht = HashTable(8)
  print(ht.arr)
  print(len(ht.arr))

  print(ht.hash_func('Matthew'))
  print(ht.hash_func('Abraham'))
