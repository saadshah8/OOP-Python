# INHERITANCE: 

# 1- Single
# 2- Multi-Level
# 3- Multiple

# Super() method is a method used to access inherit methods of parent class
# if we want to use any method f parent class we can use super method

class car():
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class toyota(car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)  
        # self.type = type
        super().start()

c1=toyota("prius","electric")
# print(c1.type) 
# it wont work, if done like this then we will have to clear an attribute like on line 70 but this attribute 
# will be only in toyota class. so we can use super() to make sure that we are using that same attribute
print(c1.type) # it will work now
