###
# filename: HighArray.py
# purpose:  @see homework02 description at:
#    https://bjohnson.lmu.build/cmsi3530web/homework02.html
# author:   Dr. Johnson
# date:     2023-01-04
###

# global to the entire file
a = []         # empty list
max = 0
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
   def display( self ):
      print( *a )        # NOTE: This is a good way to display lists
      return

   # get max goes here
   def getMax( self ):
      max = 0
      if len(a) == 0:
            return -1
      for i in range( len( a ) ):
         if a[i] > max:
            max = a[i]
      return max
   # noDupes goes here
   def noDupes( self ):
      global a
      a = [*set(a)]
      return a
   
# a little test to make sure the interpreter won't barf
h1 = HighArray( 10 )
h1.display()