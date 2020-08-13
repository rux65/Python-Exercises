import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum1=0   
    for i in range (2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            sum1+=i
           
    print (sum1)

    # the sieve method:

    #  create a list of consecutive integers 2, 3, 4,...n
    #  let p= fist number of the list 2
    #  cross out all multiplications
    #  remaining numbers are primes 


    i=2
    list1=[]
    while i<=n:
        list1.append(i)
        i+=1
    #print(list1)
    list2=list1
    
    for i in range(2,(len(list1)+1)):
        for j in range(2,(len(list1)+1)):
            if (i*j) in list2 and i*j<=n:
                list2.remove(i*j)
    #print(list2)
    product=0
    for i in range(0,len(list2)):
        product=product+list2[i]
    print(product)

    # a lesson in Python

    # iterables: read items one by one
    # example is:
    # for i in mylist:
    #       print(i)
    ##
    # another way to create lists
    # myList=[x*x for x in range(3)
    # for i in my list: ....
    ##
    # iterable store values in memory

    # generators - iterate only once
    # they do not store values in memory
    # they generate values on the fly:
    ## my_generator=(x*x for i in range(3)):
    # will print: 0, 1,4

    # yield = used like return
    # the return is a generator
    # def createGenerator():
        # my_list= range(3)
        # for i in my_list:
        #   yield i*i

    #when you call the function, the code written in the body does not run
    # function return generator object
    # https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

    
    list1=range(n)
    primes1=[]
    def primes(no):
        list2=(i for i in range(no))
        for i in list2:
            list3=(j for j in range(no))
            for j in list3:
                if i*j not in list1:
                    primes1.append(i)
    primes(n)
    print(primes1)
    

    



