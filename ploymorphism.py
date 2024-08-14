# Polymorphism, Operator Overloading

# "+" works differently with different data types
# so it is operator overloading (Polymorphism)

class complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNum(self):
        print(self.real , "i + " , self.img , "j")
    
    def add(self,number):
        addreal = self.real + number.real
        addimg = self.img + number.img
        return (complex(addreal,addimg))
    
    # dander function for operator overloading of "+"
    def __add__(self,number):
        addreal = self.real + number.real
        addimg = self.img + number.img
        return (complex(addreal,addimg))

n1=complex(1,1)
n2=complex(3,3)
n1.showNum()
n2.showNum()

n3 = n1.add(n2)
n3.showNum()
# we can't directly add two complex numbers so we will define a logic for +
# with the help fo dander functions
n4 = n3 + n1
n4.showNum()
