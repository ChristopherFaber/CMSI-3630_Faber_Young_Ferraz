"""
    An application that prompts the user for a number of eggs, and reports this
    number in grosses and dozens.
   """

import math

DOZEN = 12
DOZENSQR = 144
NONE_ZERO_VAL = 0
def instructions():        # 
      print( "\n Welcome to the Egg Counter! " )
      print( "  If you have less than a billion eggs," )
      print( "  we'll help you count them, like the pros do." )
      print( "  You must enter the number of eggs as an integer." )

def main():
      try:    # Tells the interpreter to try whatever is in this block and if it works, then "except:" does not run
         eggs = int( input( "How many eggs? " ) )
      except:
         instructions()
         print( " Please try again ")
         return
      if( eggs < 0 ):
         instructions()
         return
      elif( eggs >= 1000000000 ):
         instructions()
         return
      gross = eggs / DOZENSQR
      excessOverGross = eggs % DOZENSQR
      dozens = excessOverGross / DOZEN
      leftOver = excessOverGross % DOZEN
      if(eggs < DOZENSQR ):
           print( "You have {} gross, {} dozen, and {} eggs.\n".format( round(NONE_ZERO_VAL), round(dozens), leftOver ) )
      elif(eggs == DOZENSQR):
           print( "You have {} gross, {} dozen, and {} eggs.\n".format( round(gross), round(NONE_ZERO_VAL), leftOver ) )
      else:
           print( "You have {} gross, {} dozen, and {} eggs.\n".format( gross, dozens, leftOver ) )
main()