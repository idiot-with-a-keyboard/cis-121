from random import randint
class Die:
    def __init__(self,faces:int,value:int):
        self.faces:int=faces
        self.value=value
    def roll(self) -> None:
        self.value = randint(1,self.faces)
    def getValue(self):
        return self.value
    def __str__(self) -> str:
        return f"[{self.getValue()}]"
    def __gt__(self,other):
        return self.getValue() <= other.getValue()
    def __add__(self,other):
        return self.getValue() + other.getValue()

class Player:
    def __init__(self,name:str,dice:tuple[Die,Die]) -> None:
        self.name:str = name
        self.dice:tuple[Die,Die] = dice
        self.history:list[int] = []
    def rollDice(self):
        for i in self.dice:
            i.roll()
    def getDiceValue(self):
        return self.dice[0].getValue() + self.dice[1].getValue()
    def __str__(self) -> str:
        return f"{self.name}: {self.getDiceValue()}"

class HighTwoGame:
    def __init__(self,p1:str,p2:str) -> None:
        self.players:tuple[Player,Player] = (Player(p1,(Die(6,1),Die(10,1))),Player(p2,(Die(6,1),Die(10,1))))
        self.matches:str = ""
    def playOneGame(self):
        p1,p2 = self.players
        p1.rollDice()
        p2.rollDice()
        d1,d2 = p1.getDiceValue(),p2.getDiceValue()
        p1.history.append(d1)
        p2.history.append(d2)
        if d1 > d2:
            self.matches += "1"
        elif d2 > d1:
            self.matches += "2"
        else:
            self.matches += "t"

    def playManyGames(self,games:int) -> None:
        for i in range(games):
            self.playOneGame()
    def report(self, summarize:bool):
        p1,p2 = self.players
        if summarize:
            wins1=self.matches.count("1")
            wins2=self.matches.count("2")
            print("The score is",wins1,"to",wins2)
            if wins1 > wins2:
                print(p1.name,"wins!")
            elif wins2 > wins1:
                print(p2.name,"wins!")
            else:
                print("It's a tie!")
            return
        for i in range(len(self.matches)):
            print(f"Game {i+1}:")
            print(p1.name,"rolled a",p1.history[i])
            print(p2.name,"rolled a",p2.history[i])
            if self.matches[i]=="t":
                print("It's a tie!")
            elif self.matches[i]=="1":
                print(p1.name,"wins!")
            else:
                print(p2.name,"wins!")
            print()

if __name__ == "__main__":
    count = int(input("How many games to run? "))
    summ = input("Summarize the games?(Y/n) ").upper() != "N"
    game = HighTwoGame(input("Player 1 Name? "),input("Player 2 Name? "))
    game.playManyGames(count)
    game.report(summarize=summ)
