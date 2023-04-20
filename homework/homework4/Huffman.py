from collections import Counter
class Node():

    def __init__(self, value):
        self.letter = value
        self.left = None
        self.right = None
        self.frequency = 0

    def isLeaf(self):
       return self.left == None & self.right == None

class huffman():

   def __init__(self, string):
        string = string.lower()
        global my_string
        my_string = string
        list = [x for x in string]
        dict = {i:list.count(i) for i in string}
        key = dict.keys()
        global obj_list
        obj_list = [None] * len(dict)
        i = 0
        for x in dict:
            obj_list[i] = Node(x)
            obj_list[i].frequency = dict.get(x)
            print(obj_list[i].letter, ':', obj_list[i].frequency )
            i += 1
    
   def sort(self):
        n = len(obj_list)
        for j in range(n-1):
            for i in range(n-j-1):
               if obj_list[i].frequency > obj_list[i+1].frequency:
                  temp = obj_list[i+1] 
                  obj_list[i+1] = obj_list[i]
                  obj_list[i] = temp
               elif obj_list[i].frequency == obj_list[i+1].frequency:
                   if ord(obj_list[i].letter) > ord(obj_list[i+1].letter):
                       temp = obj_list[i+1] 
                       obj_list[i+1] = obj_list[i]
                       obj_list[i] = temp

   def display(self):
       i = 0
       for x in obj_list:
           print(obj_list[i].letter, end='')
           i+=1
       print('\n')
    
   def tree(self):
       i = 0
       while len(obj_list) > 1:
           
           NewNode = Node(None)
           NewNode.frequency = obj_list[i].frequency + obj_list[i+1].frequency
           NewNode.left = obj_list[i]
           NewNode.right = obj_list[i+1]
           NewNode.letter = str(obj_list[i].frequency + obj_list[i+1].frequency)
           obj_list[i] = NewNode
           obj_list.pop(1)
           self.sort()
       return self.traverse(obj_list[0])

   def traverse(self, root):
       global encoded_bits
       encoded_bits = ''
       for char in my_string:
           encoded_bits += self.find_huffman(root, char)
       return encoded_bits

   def find_huffman(self, node, char, code=''):
       if node is None:
           return None
       if node.letter == char:
           return code
       left_code = self.find_huffman(node.left, char, code + '0')
       if left_code:
           return left_code
       right_code = self.find_huffman(node.right, char, code + '1')
       if right_code:
           return right_code
       return None
   
   def decode(self):
       ans = ''
       encoded_list = [x for x in encoded_bits]
       curr = obj_list[0]
       n = len(encoded_list)
       print('traversal:\n')
       for i in range(n):
           if encoded_list[i] == '0':
               curr = curr.left
           else:
               curr = curr.right
           if curr.left is None and curr.right is None:
               ans += curr.letter
               curr = obj_list[0]
               print(ans)
       return ans + '\0'            

string1 = "Made by Christopher, Roberta, and Aden"
mystring = huffman(string1)
mystring.sort()
mystring.display()
mystring.tree()
print(mystring.tree())
mystring.decode()