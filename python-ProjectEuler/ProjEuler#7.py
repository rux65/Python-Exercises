import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    #nth prime
    i=0
    while i<n:
        for f in range(2, 10**5):
            for k in range(2,f):
                if f%k==0:
                    break
            else:
                prime=f
                i+=1
            if i>=n:
                break 
        print (prime)

        #10
        #2,3,5,7,11,13,17,19,23,29
       



