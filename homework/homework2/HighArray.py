###
# filename: HighArray.py 
# purpose:  @see homework02 description at:
#    https://bjohnson.lmu.build/cmsi3530web/homework02.html
# author:   Dr. Johnson
# date:     2023-01-04
###

# global to the entire file
a = []         # empty list

# the class
class HighArray():

   # fields

   # initializer
   def __init__( self, maxSize ):
      a = []         # initialize the list to be empty [still]

   # find if a value is in the list
   def find( self, value ):
      for x in a:
         if( x == value ):
            return True
      return False

   # insert a value at the end of the list
   def insert( self, value ):
      a.append( value )
      return

   # delete a specific value
   def delete( self, value ):
      a.remove( value )
      return value

   # display
   def display(self):
      print(*a)     # found syntax on https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
      return 

   # get max goes here
   def getMax(self):
      if a == []:
        return -1
      else:
        return max(a)
   # noDupes goes here
   def noDupes(self):
    # define a, where the list is stored, as a global variable so that nuDupes can access and modify it.
    global a   
    a_noDupes = [] 
    [a_noDupes.append(element) for element in a if element not in a_noDupes]
    a = a_noDupes
    # references:
    # https://stackoverflow.com/questions/74412503/cannot-access-local-variable-a-where-it-is-not-associated-with-a-value-but
    # https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
    return a

# a little test to make sure the interpreter won't barf [res.append(x) for x in test_list if x not in res]
h1 = HighArray( 10 )
h1.display()