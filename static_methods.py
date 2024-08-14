# Other methods were non static as they required self in the arguments

# STATIC METHOD:
# when we dont want a method on object level so we make it on class level by help of decorator

class peep:

    def __init__(self, name):
        self.name=name

    @staticmethod #decorator(allow to change the behavior of wrapped function w/o permanently modifying it)
    def greet(): #no self argument
        print("Welcome")
        # print(f"welcome {self.name}") can not call name like this because it doesn't know what self is

p1=peep("jacky")
print(p1.name)
p1.greet()

