'''
Keyword Arguments -----
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly when asked 
'''
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def my_data(**info):
   print("My name is ",info['fname'])
   print("My last name is ",info['lname'])
   print("My age is ",info['mage'] )  

my_data(fname="Manasi",lname ="Sharma",mage ="9")


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
