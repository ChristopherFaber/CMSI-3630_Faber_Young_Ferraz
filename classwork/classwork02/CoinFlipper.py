#
# A command line application that reports the odds of tossing a fair coin 1-10
# times and getting heads each time.
#

# We'll show odds both in "1 in n" format and in percentage format
# message = "Odds of throwing {0:4d} heads in a row is 1 in {1:7f} ({2:8.5f}%)"

possibilities = 2
tosses = int( input("How many coins will you toss?:\n"))
for tosses in range( 1, tosses + 1 ):
    #percentage = 100.0 / possibilities
    # line = message.format( tosses, possibilities, percentage )
    # line = print( f"Odds of throwing {tosses:8.5f} heads in a row is 1 in {possibilities:7d} ({percentage:8.5f}%" )
    # print( line )
    # Ready for the next iteration
    possibilities *= 2
if tosses > 10:
    print( "No chance\n")
    percentage = 100.0 / possibilities
    line = print( "Odds of throwing {} heads, in a row is 1 in {}, ({}%),".format(tosses,possibilities,percentage) )
    print( line )
else:
    print( "hm maybe...\n")
    percentage = 100.0 / possibilities
    line = print( "Odds of throwing {} heads, in a row is 1 in {}, ({}%),".format(tosses,possibilities,percentage) )
    print( line )

            