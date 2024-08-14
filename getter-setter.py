# GETTER / SETTER:

# In the Property.py example property(def ave) was working like getter as we could only get
# the value but we can not set the value as we cant do something like st1.ave = int
# getter makes a method work like a property(attribute) and it is a good example of encapsulation
class mi():
    def __init__(self,value):
        self.value = value

    def show(self):
        print(f"value is {self.value}")

    @property #getter
    def tenX(self):
        return 10*self.value

    @tenX.setter #setter
    def tenX(self,newVal):
        self.value = newVal/10

o1 = mi(10)
print(o1.tenX)
o1.tenX = 200 # can't be done like this because it is like a getter, until a setter method is defined
print(o1.tenX)