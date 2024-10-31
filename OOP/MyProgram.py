from ClassFile import *
friends:list[RoboFriend] = []

for i in range(3):
    age = input("Age of new friend:")
    name = input("Name of new friend:")
    friends.append(RoboFriend(name=name,age=age))


for i in friends:
    i.stateName()
    i.stateAge()
