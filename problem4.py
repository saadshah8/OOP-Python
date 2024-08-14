# Problem 4: create class order and then create a method to check which order is greater by price

class order():
    def __init__(self, name, pr):
        self.name = name
        self.pr = pr
    
    def gt(self,or2):
        return (self.pr > or2.pr)
    
    def __gt__(self,or2):
        return (self.pr > or2.pr)
    
o1=order("milk",10)
o2=order("water",5)

#by the gt defined method
print(o1.gt(o2))

# directly by dander function
print(o1>o2)