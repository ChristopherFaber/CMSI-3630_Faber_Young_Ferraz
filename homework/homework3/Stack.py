# DATA STRUCTURES HW#4
# DATE: March 19, 2023
# 4
'''
Implement a stack class based on the circular list of Programming Project 5.3.
This exercise is not too difficult.
[However, implementing a queue can be harder, unless you make the circular list doubly linked.]
'''

class Stack():
    # LIFO STRUCTURE
    # LISTS are used to implement the stack
    # right of the list represents tht top of the stack.
    def __init__(self):
        self.nItems = 0
        self.stack_view = []
        self.pointer = 0 # pointer always points to the top of the stack. 
        self.next_available = 0
        return
    

    def insertion(self,item):
        # special case for when the first item is added
        if len(self.stack_view) == 0:
            self.pointer = 0
            self.next_available = 1
            self.stack_view.append(item)
        else:
            self.stack_view.append(item)
            self.pointer += 1
            self.next_available += 1
        return
    
    def deletion(self):
        # when the stack is empty print error message
        if len(self.stack_view) == 0:
            self.pointer = 0
            self.next_available = 0 # if stack is empty, pointer and next_available point to the same index.
            return print("Stack is empty, can't remove an item.")
        else:
            self.stack_view.pop( len(self.stack_view) - 1 ) # remove last item added
            self.pointer -= 1
            self.next_available -= 1

            if self.pointer == -1:
                self.pointer = 0
                return
            return

    def disp(self):
        return print(self.stack_view)
    
def main():
    s1 = Stack()
    s1.insertion(0)
    s1.insertion(1)
    s1.insertion(2)
    s1.disp()
    s1.deletion()
    s1.disp()
    s1.deletion()
    s1.disp()
    s1.deletion()
    s1.disp()
    s1.deletion()
    s1.disp()

main()
