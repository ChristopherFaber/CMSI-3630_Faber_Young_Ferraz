import math

number_of_rows = 64
frequency = 16.0
amplitude = 12
for row in range( number_of_rows ):                                            # Always end the range right after the max number you want (i.e. if you want 63 #'s, make the range go til' 64)
   waveHeight = math.fabs( math.sin( row * math.pi / frequency ) + 1 )
   numberOfStars = int( round( amplitude * waveHeight, 0 ) )
   for col in range( numberOfStars ):                              # The second for loop inside of this for loop together constitute a nested loop
      print( "*", end = "" )                                       # This prints *'s until it reaches the end of the string which is denoted by the plus sign and empty quotes together
   print()
