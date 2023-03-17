class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.sizeCount = 0
        self.maxSize = 0
        self.queArray = []
        self.nItems = 0
    def queue(self, s):
        self.maxSize = s
        self.queArray = [None] * s
        # self.nItems = s - 1
    def insert(self, i):
        if self.rear >= self.maxSize-1:            
           self.rear = 0
           return print("list is full")
        else:
           self.rear += 1
           self.queArray[self.rear] = i
           self.nItems += 1
           return self.queArray
    def remove(self):
        if self.front >= self.maxSize-1:
           self.front = 0
           return print('list is empty')
        else:
           self.front += 1
           self.queArray[self.front] = None
           self.nItems-=1
        return 
    def peekFront(self):
        return self.queArray[self.front]
    def isEmpty(self):
        if bool(self.queArray):
            return True
        else:
            return False
    def isFull(self):
        if bool(self.queArray):
            return False
        else:
            return True
    def size(self):
        return self.nItems
    def display(self):
        temp = [x for x in self.queArray if x != None]
        print(temp)
        # print(self.queArray)
        

myQueue = Queue()
myQueue.queue(6)

myQueue.display()
myQueue.insert(10)
myQueue.display()
myQueue.insert(20)
myQueue.display()
myQueue.insert(30)
myQueue.display()
myQueue.insert(40)
myQueue.display()
myQueue.insert(50)
myQueue.display()
myQueue.insert(60)


myQueue.display()
myQueue.remove()
myQueue.display()
myQueue.remove()
myQueue.display()
myQueue.remove()
myQueue.display()
myQueue.remove()
myQueue.display()
myQueue.remove()




   


