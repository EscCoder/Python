'''
Given an array, arr[] and a positive integer K. 
The task is to find the position say i of the element in arr[] such that 
prefix sum till i-1, i and suffix sum till i+1 are in Geometric Progression with common ratio K.
'''


##verify if GP or not ##########################3
arr=[-3,5,0,2,1,25,25,100]
k = 5

element=0

l=len(arr)
#print(l)
for i in range(0,l):
   element = arr[i]
   three_num =[]
   check=[]
   #print("elem",element)
   three_num.append(element)
   
   pre_sum=0
   sufx_sum=0
   
   for p in range( 0,i):
      pre_sum = arr[p]+pre_sum
   #print("presum",pre_sum)
   three_num.append(pre_sum)

   for s in range(i+1, l):
      sufx_sum = arr[s]+sufx_sum
   #print("sufix",sufx_sum)
   three_num.append(sufx_sum)
   #print (three_num)
   check=sorted(three_num)
   #print(check)

   if check[1]== check[0]* k  and check[2]==check[1]*k :
      print(check,"is a GP and the element is ",arr[i])
      print(i+1,"is the elements position")
       

##########################################3
 
