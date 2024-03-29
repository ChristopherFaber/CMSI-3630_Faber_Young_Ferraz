###
# filename: HighArrayTest.py
# purpose:  @see homework02 description at:
#    https:#bjohnson.lmu.build/cmsi3530web/homework02.html
# author:   Dr. Johnson
# date:     2023-01-04
###

from HighArray import HighArray

print( "\n   Welcome to the HighArray Program [Python Version]" )
print( "   =================================================" )
print( "   Initializing the list" )
arr = HighArray( 100 )
print( arr )

print( "   Adding ten items" )
arr.insert( 77 )                 # insert 10 items
arr.insert( 99 )
arr.insert( 44 )
arr.insert( 55 )
arr.insert( 22 )
arr.insert( 88 )
arr.insert( 11 )
arr.insert( 00 )
arr.insert( 66 )
arr.insert( 33 )

print( "\n   Current list contents:" )
arr.display()
# TODO: put in a call to 'arr.getMax()'
print("\nThe highest value in the list is: ")
print(arr.getMax())

print( "\n   Searching for 37:" )
found = arr.find( 37 )
if( found ):
   print( "Found it!" )
else:
   print( "Bummer, dude..." )

print( "\n   Searching for 11:" )
found = arr.find( 11 )
if( found ):
   print( "Found it!" )
else:
   print( "Bummer, dude..." )

print( "\n   Adding and removing to test getMax function..." )
arr.delete( 00 )          # delete 3 items
arr.delete( 55 )

max_numb = arr.getMax() #finding the maximum value in the list and storing it in max_numb.
arr.delete( max_numb )  # deleting the highest value.

arr.display()             # display items again
print("\n the number {} was removed from the list, now the largest number in the list is: {} ".format(max_numb, arr.getMax()))

print( "\n   Adding 11, 00, 66, and 33 to make duplicates..." )
arr.insert( 11 )
arr.insert( 00 )
arr.insert( 66 )
arr.insert( 33 )
arr.display()
print( "\n   Removing dupes ")
arr.noDupes()
arr.display()
print( "\n   Adding five copies of 33..." )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.display()
print( "\n   Removing dupes")
arr.noDupes()
arr.display()
print("\nThe highest value is: ", arr.getMax())
print('Final Test:\nremove all elements from the list and check if arr.getMax() returns -1')
arr.delete( 77 )
arr.delete( 44 )
arr.delete( 22 )
arr.delete( 88 )
arr.delete( 11 )
arr.delete( 66 )
arr.delete( 33 )
arr.delete( 0 )
print("\nREMOVED ALL ELEMENTS FROM THE LIST.\nHIGHEST VALUE IS: ", arr.getMax())

print( "\n   TESTING COMPLETE!  THANKS FOR DROPPING BY..." )