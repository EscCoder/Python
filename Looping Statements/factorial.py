"""
Factorial of a number
"""

#to take input 
num = int (input("Enter a number : ")) 

fact = 1
#to start from one

#for function is always written as
   #in range (start,end=n-1):

  
for i in range (1,num+1):#here we need the num also
  fact = fact*i

#to print outputs
print(fact,"is factorial of ",num)
