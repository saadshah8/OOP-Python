
# CLASS METHODS: ()
# Static methods cant access class states or attributes, only used for utility
# here we want to change the class attribute name and also the method attribute name
class person():

    name = "Anonymous"

    def __init__(self,name=None):
        if name != None:
            self.name = name
        else:
            self.name = person.name

    def changeName(self, name):
        self.name = name

    @classmethod # class method decorator
    def changeName(cls, name):
        cls.name = name

p1=person("jacky")
p2=person("micky")
p3=person()
p2.changeName("mickey")
print(p1.name)
print(p2.name)
print(p3.name)
print(person.name)
print("//////////////////////")
person.changeName("jackymarr")
print(p1.name)
print(p2.name)
print(p3.name)
print(person.name)

