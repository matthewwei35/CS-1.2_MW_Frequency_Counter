from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):
    current = self.head
    found = False
    counter = 0

    while current != None and not found:
      if current.data[0] == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      pass
    else:
      return -1


  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def check_if_key_exists(self, key):
    """Checks if the given key exists in the linked list, if it does exists, remove the old tuple, 
    and create a new tuple with updated value by adding one. If it does not exist, just create a n-
    ew tuple and append it to the linked list."""
    current_tuple = self.head
    found = False

    while current_tuple != None and not found:
      if current_tuple.data[0] == key:
        found = True
      else:
        current_tuple = current_tuple.next
    
    if found:
      number_of_occurrence = current_tuple.data[1]
      new_tuple = (current_tuple.data[0], (number_of_occurrence + 1))
      current_tuple.data = new_tuple
    else:
      return -1


  def print_nodes(self):
    current = self.head
    
    if current == None:
      pass
    else:
      for i in range(self.length()):
        print(f'{current.data[0]}: {current.data[1]}')
        current = current.next
