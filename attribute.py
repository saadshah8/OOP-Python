# the objects created in the destructors occupy spaces as in every object will occupy their 
# own new space in the memory. No if we have a scenario where every objects occupation is same but the 
# names are different, so giving individual memory to every objects's occupation is memory wastage,
# what we can do is that we can create a class attribute occupation and for every object that attribute will be 
# initialized and also there will be single space for occupation attribute, not for every object individually.

class human():
    occupation = "Engineer"
    def __init__(self, name): # Parameterized Constructor
        self.name = name
    def info(self):
        print("Name: {} | Occupation: {}".format(self.name, self.occupation)) #self.occupation can be written as human.occupation because is a class attribute
    

human_1 = human("jake") #constructor is invoked whenever an object is made
human_1.info()
 
human_2 = human("james")
# print("The name if student is: ", human_2.name ," | The occupation is: ", human_2.occupation) #human_2.occupation can be written as human.occupation because is a class attribute
print(human_2.name , human.occupation)