import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n==1 or n==2 or n==0:
            print(n)
    else:
            i=2
            primes=[]
            while i<=n:
                    for k in range(2,i):
                            if i%k==0:
                                    break
                    else:
                        primes.append(i)
                    i+=1
            #print(primes)
            l=2
            divisors=[]
            for l in range(2,n+1):
                #if l not in primes:
                for j in primes:
                    if l%j==0:
                        l=l/j
                        divisors.append(int(j))
            #print(divisors)         
            # case 20:[[], [], [2], [], [2, 3], [], [2], [3], [2, 5], [], [2, 3],
            #[], [2, 7], [3, 5], [2], [], [2, 3], []]
	    # strip duplicates 
	    # unfinished	
            #list1=[]
            #for i in divisors:
            #    if i not in list1 and i!=[]:
            #        list1.append(i)
            #print (list1)

            list2=[]
            for i in divisors:
                if [i,divisors.count(i)] not in list2:
                    list2.append([i,divisors.count(i)])
            #print(list2)
            for j in list2:
                #print(j)
                for k in range(0,j[1]+1):
                    if j[0]**k<=n:
                        #print(j[0]**k)
                        j[1]=k
                        if j[1]==0:
                            j[1]=1
            #print(list2)
            product=1
            for i in list2:
                product=product*i[0]**i[1]
                #print (i, i[0], i[1], "p")
                
               
                
            #print(product)
            #for j in primes:
            #    if j not in divisors
            #        product=product*j
            print(product)
			
			
			
			
			
    
            #m=1
            #m1=1
            #for j in primes:
                    #if j not in divisors:
                            #m=m*j
            #print(m)
            #for ma in divisors:
                   #m1=m1*ma
            #print(m1)
            #print (m*m1)

            # 20
            # 1,2,3,2,5,7,2,3,11,13,2,17,19
            #print (2**4*3**2*5*7*11*13*17*19)
            #232792560

            #5
            #2,3,2,5
            #60

            #7
            #2,3,2,5,7
            #420


