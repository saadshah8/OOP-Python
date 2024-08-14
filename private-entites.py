# PRIVATE ENTITIES: ( __Method , __attribute )
# objects or methods that can only be used within the class and are not accessible from outside the class

class bank_account():
    def __init__(self, name , pin):
        self.name = name
        self.__pin = pin
    
    # def info(self): #public method
    def __info(self): #private method
        print(f"Name: {self.name} | Pin: {self.__pin}")
    
    def all(self):
        return(self.__info())
    
p1 = bank_account("Sam" , 1020)
print(p1.name)
# print(p1.__pin) it will output as no attribute because its private and can only be accessed within class

#p1.info()   # now we can see that __pin was accessed outside the class by a public method function, 
            # the method was public and also method can access the private attributes within the class

#p1.__info() # now ill make info a private method and it wont be accessible directly outside the class,
            # so i will call it with the help of another method to clear up the concepts

p1.all()    #accessing a private attribute of a private method by a public method
