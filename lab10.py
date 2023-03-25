#Lab 10
class RoboFriend:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def stateName(self):
        print("Hello. My name is",self.name)
    def stateAge(self):
        print("I'm",self.age,"years old")

friend1=RoboFriend("Saron",16)
friend2=RoboFriend("Drancula",17)
friend3=RoboFriend("Franz",18)
friend1.stateName()
friend1.stateAge()
friend2.stateName()
friend2.stateAge()
friend3.stateName()
friend3.stateAge()

