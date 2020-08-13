## largest 6 digit palindrome that is a product of 2 3 digit numbers

# 2 lists - 100-999 and starting backwards 999999 to 100 000
# if the number is divisible by 100,000 it's excluded
# what is the range of multiplications by 3 digits that exceeds 6 digit?
## if we have 999 then the other is 999 - 998,001
## next pallindrome is 997799
## smallest pallindrome 101101

## not universal but we want to check that position 0=5, 1=4 2=3
##we want to exclude numbers divisible by 100,000
## we want range 101101 to 997799
## we want number to be divisible by over other primes
## we start from 997799 and stop when we find one
## we take divisors and multiply untill we reach 100
## if one divisor is > 3 digits we stop and go to the next number



import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    li=[]
    for i in range(n,99999,-1):
        if (str(i)[0]==str(i)[5] and str(i)[1]==str(i)[4] and str(i)[2]==str(i)[3]):
            #print(i)
            for j in range(999,142,-1):
                #print(j)
                if i%j==0:
                    if i/j<=999:
                        li.append(i)
                        break
    print (li[0])                   
                    

## how can I make this break after the first instance
    
            
            
                
