# CONSTRUCTORs
human_count = 0
class human():

    # Constructor(to initialize values)
    
    def __init__(self): # default constructor
         print("Inside the Constructor")

    def __init__(self, name, occupation): # Parameterized Constructor
        global human_count
        human_count += 1
        print(f"object {human_count} is initialized")
        self.name = name
        self.occupation = occupation
    
    # Method
    def info(self):
        print("Name: {} | Occupation: {}".format(self.name, self.occupation))

human_1 = human("jake" , "ML Engineer") #constructor is invoked whenever an object is made
human_1.info()

human_2 = human("james" , "UI/UX")
print("The name if student is: ", human_2.name ,"and the occupation is a secret.")
