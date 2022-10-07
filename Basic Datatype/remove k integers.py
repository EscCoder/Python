"""
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.

"""
"""
We have a number, say a 5 digit number 
and we are to make smallest posible number after removing 2 digits 
new_num = 5-2 =3
 the possible numbers which can be formed are 3 digit numbers or less if zeros are included
 so by permutations we can find all possible such numbers  
 
 after getting an array of all the possible 3digit numbers which can be formed
 we can compair them to find the smallest among them 
 """

str_num = input("Enter a number: ")
digi_list=[]

for i in str_num:
   digi_list.append(i)
print("The digits we need to use are ",digi_list)



