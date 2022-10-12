 '''
Fibonacci series  
1 ,1 , 2, 3 ,5 ,8 ,13 ,21 .........
'''

#first two terms
a=1
b=1

num = int (input("Enter the number of terms you need in the series :"))

#to first print 1,1
print(a)
print(b)

#to make the program work for the given range

for i in range (1,num-1): 
#num-1 as we have already printed 1,1

   c=a+b                  #according to fibonacci series
   print(c)               
   a,b= b,c               #to switch the terms and then progress
