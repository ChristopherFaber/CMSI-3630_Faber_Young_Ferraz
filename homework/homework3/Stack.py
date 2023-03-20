class Link(object) :
    Data = 0
    next = None
    def __init__(self, value) :
        self.Data = value
    def displayLink(self) :
        print(str(self.Data) + " ", end ="")
class FirstLastList(object) :
    first = None
    last = None
    def __init__(self) :
        self.first = None        # Defines 'first' and 'last' within the object FirstLastList
        self.last = None
    def  isEmpty(self) :         # Determines if the list is empty and returns the first variable if it is
        return self.first == None
    def  isFull(self):           # Tells user if the list is full
        if self.first == None:
           print('List is empty')
        else:
           print('List is not empty')
    def insertFirst(self, value) :         # Method for insertion
        newLink = Link(value)              # Instantiates the Link object as 'newLink'
        if (self.isEmpty()) :
            self.last = newLink            # If the list is empty, the first item in becomes the last item out
        newLink.next = self.first          # Next link is the first
        self.first = newLink              
    def insertLast(self, value) :          # Inserts item in the last position of the list
        newLink = Link(value)
        if (self.isEmpty()) :              # Checks if the list is empty
            self.first = newLink           # Inserts new link in the first position if list is empty
        else :
            self.last.next = newLink       # Inserts new link as the current 'last' links next link
        self.last = newLink                # New link is now the last link
    def  deleteFirst(self) :               # Method deletes data in the first position
        temp = self.first.Data             
        if (self.first.next == None) :
            self.last = None
        self.first = self.first.next
        return temp
    def displayList(self) :                # Method displays the list
        print("List (first-->last): ", end ="")
        current = self.first
        while (current != None) :
            current.displayLink()
            current = current.next
        print("")

MyList = FirstLastList()
MyList.insertFirst(22)
MyList.insertFirst(44)
MyList.insertFirst(66)

MyList.insertLast(11)
MyList.insertLast(33)
MyList.insertLast(55)

MyList.displayList()

MyList.deleteFirst()
MyList.deleteFirst()

MyList.displayList()

MyList.isFull()

MyList.deleteFirst()
MyList.deleteFirst()
MyList.deleteFirst()
MyList.deleteFirst()

MyList.isFull()