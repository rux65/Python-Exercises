import sys
from math import sqrt


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    
    #no=[]
    #for i in range(1,n//3+1):
    #    for j in range(1,i):
     #       if i**2+j**2==(n-i-j)**2:
      #          no=[n-i-j,j,i]
                #print(k,j,i)
    
    #if no==[]:
     #   print(-1)
    #else:
        #print(no)
        #print(no[0]*no[1]*no[2])                       
            
    #6,8,10    #24
    #36,77,85   #198
    #print(sqrt(36**2+77**2))

    no1=[]   
    for i in range (1,n//3):  # 3 squares,
        a=(n**2-2*n*i)/(2*(n-i))
        if a%1==0 and a>0:
            #print(a)
            if a**2+i**2==(n-i-a)**2 and a>0:
                no1=[a,i,(n-i-a)]
           
    if no1==[]:
         print(-1)
    else:
        #print(no1)
        print(int(no1[0]*no1[1]*no1[2]))  



    



