# Class/Blue print
class person():
    name = "default name"
    occupation = "default occupation"

    # Methods
    def information(self): #self is must when defining method in class
        print(f"{self.name} is a {self.occupation}")

# Objects
a=person()
a.information()
a.name = "Jake"
a.occupation = "ML Engineer"
print(f"name: {a.name},  occupation: {a.occupation}")
# print("name: {}, occupation: {}".format(a.name, a.occupation))

b=person()
b.name = "james"
b.occupation = "UI/UX"
b.information()