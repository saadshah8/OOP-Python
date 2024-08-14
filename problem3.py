# Problem 3: create class employee and then create class engineer as a child class
class emp():
    def __init__(self,role,dep,sal):
        self.role=role
        self.dep=dep
        self.sal=sal

    def details(self):
        print(f"role: {self.role}  | dep: {self.dep} | sal: {self.sal}")

class eng(emp):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","Civil","120,000")
    
    def details(self):
        print(f"name: {self.name}  | age: {self.age}")
        super().details()
        # print(f"role: {self.role} | dep: {self.dep} | sal: {self.sal} | name: {self.name} | age: {self.age}")

e1 = emp("mechanic","mechanical","100,000")
e1.details()
print("/////////////////////////")
e2 = eng("Jake","33")
e2.details()