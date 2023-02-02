from cmath import sqrt
import math
import random

MAX_DARTS = 1000000   # Max darts thrown
darts = 0   # Sets initial dart count
inCirc = 0   # Sets darts in circle

for darts in range(MAX_DARTS):   # Check if max darts has been reached
   x = random.uniform(0, 1)   
   y = random.uniform(0, 1)
   hyp = math.sqrt(x ** 2 + y ** 2)
   darts = darts + 1
   if (hyp <= 1):   # Check if dart is in circle
      inCirc = inCirc +1

pi = 4 * ( inCirc/MAX_DARTS )
print( "pi is approximately: ")
print( pi )


      

