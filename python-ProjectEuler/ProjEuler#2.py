## adding even fibonacci  numbers

import sys


t = int(input().strip()) ## case study number
for a0 in range(t):
    n = int(input().strip()) ## input till which number we go
    i=0
    m=1
    sum1=0
    while i<=n or m<=n:
        if (i%2==0):
            sum1=sum1+i
        if m>n:
            break
        if (m%2==0):
            sum1=sum1+m
        i=i+m
        if i>n:
            break
        #print(i)

        m=m+i

        #print(m)
    print (sum1)

        # if i=0 then i+m  becomes 1 and m becomes 1+1 = 2 i=1, m=2
        # if i is even the add to sum ( i=1 so no)
        # i=i+m i=3 and m=2+3 = m=5 ( i=2 so not even)
        # i increses by m, i=3+5=8 and m =5+8 = 13
        # if i is even then test
        # i =4
		
		##success!