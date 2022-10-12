"""
to find element in a given array
"""

#function to find the element
def linear_search(arr,x):
   for i in range(len(arr)):
      if arr[i]== x:
         print("element ",x,"found at index",i)
 

#predefined array
arr=["a","b","c","d","e"]

#element to find
x = "d"
print(linear_search(arr,x))
