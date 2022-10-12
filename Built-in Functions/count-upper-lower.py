'''
Count the number of upper and lower case alphabets in the given string
use of 'islower' and 'isupper' built in functions

'''

my_str= input("Enter a string :")
low=0
upp=0

l=len(my_str)

for i in range(l):
  if my_str[i].islower():
    low = low+1
  elif my_str[i].isupper() :
    upp = upp+1
    
print("There are ",low,"lower case alphabets and",upp,"upper case alphabets")
  
