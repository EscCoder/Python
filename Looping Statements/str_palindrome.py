'''
To check if a given number is a palindrome or not 

---reverse the string and compair

'''

/////////////////////////////////////////////////////////////////////////////////////////////


def check(str_1):
   rev_str = str_1[ : : -1]

   if rev_str == str_1:
      print ("The given string is a pallindrome")
   else:
      print("The string is not a pallindrome")

str_1 = input("Enter a string: ")
check(str_1)


////////////////////////////////////////////////////////////////////////////////////////////////
