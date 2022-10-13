'''
to verify if a given number is prime or not
'''


##prime number program

num = int(input("Enter a number : "))

flag= True

for i in range (2,num):
   if num%i == 0 :
      flag=False 

if flag==True:
   print("Your number is prime")
else :
   print("Your number is composite")
