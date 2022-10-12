'''
problem statement --> 
  create a child class 'bus' that will inhert all the variables and methods from parent class 'vehical' 
'''

----------------------------------------------------------------------------------------------------------------
class vehical:
#this is the parent class

  #the arguments are sent here
  def info_format(self,model,colour,cost):
    self.model = model
    self.colour= colour
    self.cost  = cost
 

class bus(vehical):
#this is child class
  
  #a child function can access parent parametrs (variables)
  def bus_data(self):
    print("Bus information :")
    print("Model is: ",self.model)
    print("Colour is: ",self.colour)
    print("Cost is: ",self.cost)
  
#an object associated with child class bus  
x = bus()

#passing parameters to parent function
x.info_format("Mercedes-Benz","Black","85-lac")


print(x.bus_data)

----------------------------------------------------------------------------
