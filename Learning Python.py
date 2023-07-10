#Learning Python

fruits = ['apple', 'banana', 'grape', 'grape']
count =0
for ans in fruits:
    if ans == 'grape':
        count+=1
print(count)

#Learning Python
#classes and objects 
#example 
class MyClass:
    x = 5

    def function(self):
        print("this is a message")

#creating an object
someObjectx = MyClass()
print(someObjectx.x)

#demonstrating the function
someObjectx.function()

#Class for a vehicle
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." %(self.name,self.color,self.kind,self.value)
        return desc_str
    
car1 = Vehicle()
car1.name = "Tesla"
car1.color = "red"
car1.kind = "Model S"
car1.value = 60000.00

print(car1.description())