import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # sum of squares till n is given my n*(n+1)*(2n+1)/6
    # sum of first n numbers i n(n+1)/2
    sum1=0
    square=0
    sum1=n*(n+1)*(2*n+1)/6
    square=(n*(n+1)/2)**2
    difference= abs(int(sum1-square))

    print (difference)
    #2
    #1+4=5
    #9-5=4

    
        



