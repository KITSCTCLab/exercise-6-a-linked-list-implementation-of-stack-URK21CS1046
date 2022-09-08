class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
    alex_node = Node(data)
    alex_node.next = self.head
    self.head = alex_node

  def pop(self) -> None:
    # Write your code here
    temp = self.head
    if temp != None:
      self.head = temp.next
      

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  
    


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
