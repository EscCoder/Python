"""
Check if the given number is a Armstrong num or not

"""

num=n=int (input("Enter a number :"))
rev_no=0

while num!=0:
   digit = num % 10 
  
   rev_no = (rev_no * 10) +digit

   num = num//10
  

if n==rev_no:
   print(n,"Is an Armstrong number")
else :
   print(n,"Is not an Armstrong number ")
