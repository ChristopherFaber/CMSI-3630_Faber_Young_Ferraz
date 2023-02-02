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

print( "Lets check that the list is empty \n", arr.getMax() )
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
print( "max:", arr.getMax() )

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
arr.delete( 99 )
arr.display()             # display items again
# TODO: put in a call to 'arr.getMax()'
print( "max:", arr.getMax() )
arr.insert( 111 )  
print( "\n   Lets test it again..." )
arr.display()
print( "max:", arr.getMax() )
arr.insert( 22 )  
print( "\n   One last time..." )
arr.display()
print( "max:", arr.getMax() )
arr.insert( 99 )
print( "\n   Adding 11, 00, 66, and 33 to make duplicates..." )
arr.insert( 11 )
arr.insert( 00 )
arr.insert( 66 )
arr.insert( 33 )
arr.display()
print( "\n   Removing dupes")
arr.a = arr.noDupes()
arr.getMax()
arr.display()
print( "\n   Adding five copies of 33..." )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.display()
print( "\n   Removing dupes")
arr.a = arr.noDupes()
arr.display()
print( "\n   TESTING COMPLETE!  THANKS FOR DROPPING BY..." )