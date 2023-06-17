class Construct:
    def __init__(self,a,g):   #parameterized constructor
       self.age=a
       self.gender=g
    def show(self):
        print('Age :',self.age)
        print('Gender :',self.gender)

print("Show Details")

c1=Construct(18,'Female')
c1.show()

c=Construct(21,'Male')
c.show()
