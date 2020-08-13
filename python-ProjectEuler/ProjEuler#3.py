## first define all the primes till that number
## from 3 onwards
## if number is divisible by prime, then largest prime is that number

## downside is having to go through the cases till till that number while:
## it would be less time consuming to divide by the first prime then result
# divide again and if not then next one
# the one case it will go through all the iterations if the number itself is a long prime
## and has no choice but to go through all

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n= int(input().strip())
    if (n==2 or n==1 or n==0):
        print (n)
    elif n>2:
        largest=2
        i=2
        while i<=n:
            no=0
            for k in range(2,i//2+1): # 0 to halfway +1
            # if n is divided to any number then k increases
                if i%k==0:
                    no+=1
            if no<=0 and n%i==0 and largest<i: # if this is a prime
                largest=i
                
            i+=1
        print (largest)
                

## some timeouts
# need to make the code quicker to run
# almost want to half it - check second half first
# if not in the first half then second


#!! error: I have case where number 997799 was given where the
#highest number is 90709 which is a prime
# yet I get 11
# it doesn;t go forward.


            
        
