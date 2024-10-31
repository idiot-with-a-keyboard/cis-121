class RoboFriend:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
    def stateName(self):
        print(f"Hello, my name is {self.name}.")
    def stateAge(self):
        print("I'm", self.age, "years old!")

