class Node:

    def __init__(self, value):
        self.data = value
        self.next = None
    
class circularList:

   def __init__(self):
       self.head = Node(None)
       self.tail = Node(None)
       self.head.next = self.tail
       self.tail.next = self.head
       self.nItems = 0
       self.current = None
       
   def insertion(self, value): 
       NewNode = Node(value)
       if self.nItems == 0:
           self.head = NewNode
           self.tail = NewNode
           self.current = NewNode
       else:
           self.tail.next = NewNode
           self.tail = NewNode
           self.tail.next = self.head
       self.nItems += 1

   def display(self):
       if self.nItems == 0:
          print('List is empty')
       else:
          for i in range(self.nItems):
              self.current = self.current.next
              print(self.current.data)
          
   def search(self, value):
       temp = [] * self.nItems
       node1 = self.head
       if self.nItems == 0:
          print('List is empty')
       else:
          for i in range(self.nItems-1):
              temp.append(node1.data)
              node1 = node1.next
       if value in temp:
          print('Value is present in list')
       else:
          print('Value could not be found')
    
   def printCurrent(self):
        print("Head:", self.head.data)

   def step(self):
       window = self.head
       self.head = self.head.next
       return print('Head:', self.head.data)

   def remove(self, value):
       node1 = self.head
       if node1.data is value:
           self.tail.next = node1.next
           self.head = self.head.next
       else:
           while (node1.data != value):
              node1 = node1.next
           for i in range(self.nItems-1):
              node1 = node1.next
           self.tail.next = node1.next.next
       self.nItems -= 1

circularList1 = circularList()
circularList1.insertion(1)
circularList1.insertion(2)
circularList1.insertion(3)
circularList1.insertion(4)
circularList1.display()
circularList1.printCurrent()
circularList1.step()
circularList1.step()
circularList1.step()
circularList1.search(1)
circularList1.search(23)
circularList1.remove(1)
circularList1.display()
circularList1.printCurrent()
circularList1.search(1)
circularList1.remove(2)
circularList1.display()
circularList1.search(2)
circularList1.remove(3)
circularList1.display()
circularList1.remove(4)
circularList1.display()
