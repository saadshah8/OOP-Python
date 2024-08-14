# DELETE KEYWORD:

class person():
    def __init__(self,name):
        self.name=name

p1=person("mickle")
# print(p1)
print(p1.name)
# del p1 deleting an object
del p1.name #deleting an object's attribute
# print(p1)
print(p1.name)