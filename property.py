# PROPERTY:

class stu:
    def __init__(self, phy, chem):
        self.phy = phy
        self.chem = chem
        # self.ave = "Average : " + str((self.phy +self.chem)/2) + " marks" # making it a string

    # def calcAve(self):
    #     self.ave = "Average : " + str((self.phy +self.chem)/2) + " marks" # making it a string

    @property
    def ave(self):
        return ("Average : " + str((self.phy +self.chem)/2) + " marks") # making it a string
        # the returned value is now converted into a property(attribute)

st1 = stu(12,21)
print(st1.ave)

st1.phy = 14
# st1.calcAve()
print(st1.phy)
print(st1.ave) # now ave is a property not a method so don't code it like st1.ave()
# It can be seen that phy masks are changed but this change is not reflect in the average
# until we write this: st1 = stu(14,21), or make an individual method to calculate average
# and call that method explicitly for that object
# so we'll make it correct by property decorator

# when value of attribute depends on function, we make that function a property(attribute)

# now i dont have to explicitly call the method, and when i will change
# the marks of subject it will be reflected in the Average method too
# making a new property method
