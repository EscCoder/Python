'''
given three numbers arrange them in the ascending order
'''
#to print largest of 3 numbers
#using functions
def largest(a,b,c):
   #if conditions
   if ( a>=b) :
      if ( b>=c):
         print("{0} > {1} > {2} =1 ".format( a,b,c))
      else :
         #here c>=b
         if ( a>=c):
            print("{0} > {1} > {2} =2 ". format( a,c,b))
         else:
            #c>=a
            print('{0} > {1} > {2} =3 '.format(c,a,b))
   else :
      #executed as b>=a
      if ( a>=c):
         print('{0} > {1} > {2} = 4 '.format(b,a,c))
      else:
         #c>=a
         if (c>=b):
            print('{0} > {1} > {2} = 5 '.format(c,b,a))
         else:
            #b>=c
            print('{0} > {1} > {2} = 6'.format(b,c,a))
   
#output will not be printed if return is not given
   return 
#the actual start of program
###############
#initialize variables      
b=100
c=70
a=40     
      
#function call      
largest(a,b,c)
