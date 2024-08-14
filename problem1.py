# Problem 1: make student and take the name and marks and calculate the average and returns it
class student():
    # constructor
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    
    # method
    def information(self):
        print("Student name: {} | Marks: {} | Average marks: {}".format(self.name,self.marks,self.average()))

    def average(self):
        average = sum(self.marks)/len(self.marks)
        return average
    
s1=student("Mike",[1,2,3,4])
s1.information()
print(s1.average())
