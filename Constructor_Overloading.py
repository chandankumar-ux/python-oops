class Person:
    def __init__(self,name,age=None,address=None):
        self.name=name
        self.age=age
        self.address=address
        
    #name only
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

p1=Person("Chandan")
p2=Person("RAJ",22)
p2.display()