'''
WAP to merge two dictionaries
'''
------------------------------------------------------------------------------------------
def merge(space,items):
   for i in items:
      space[i]=items[i]
   return space


dict1 ={'a':1,'b':2}
dict2={'c':3,'d':4}

dict3={}


merge(dict3,dict1)
merge(dict3,dict2)
print("Merged dictionary is ",dict3)

/////////////////////////////////////////////////////////////////////////////////////////
