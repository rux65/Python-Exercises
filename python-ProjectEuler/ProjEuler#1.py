##Version 1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i=0
    sum1=0
    for i in range(n):
        if(i%3==0 or i%5==0):
            sum1=sum1+i
    print (sum1)

#if 100 then we need to do all the multiples of 3 till 100+ all muliples of 5 till then
# if no = 98 - then 95/5=19
# so till 95 I have 5+5*2+5*3+.....+5*19
# or 5*(1+2+3+4+5...)
#same for 3
# check overlaps

##version2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i=0
    sum1=0
    for i in range(5):
        if ((n-1-i)%5==0):
            x=(n-1-i)/5
            #print(x)
    for i in range(3):
        if ((n-1-i)%3==0):
            y=(n-1-i)/3
    for i in range(n):
        if (i%5==0 and i%3==0): # or i%15==0
            sum1=sum1+i
    print (int(5*((x*(x+1))/2)+3*(y*(y+1)/2)-sum1))

# problem -code too slow
# on hacker rank - timeout - in the future look for options
# to make it faster

# version 2 - improve on speed

## try to remmove the divisible by 5 in the 3s

# version3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i=0
    sum1=0
    for i in range(5):
        if ((n-1-i)%5==0):
            x=int((n-1-i)/5)
            #print(x)
    for i in range(3):
        if ((n-1-i)%3==0):
            y=int((n-1-i)/3)
    for i in range(0,y+1):
        if (i%5==0):
            sum1=sum1+i*3
    print (int(5*((x*(x+1))/2)+3*(y*(y+1)/2)-sum1))

## quicker but still time out
