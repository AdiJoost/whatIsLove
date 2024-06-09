from random import uniform

class Lover():

    def __init__(self, chanceToFindLove, chanceToLoseLove, inLove=False) -> None:
        self.chanceToFindLove = chanceToFindLove
        self.chanceToLoseLoce = chanceToLoseLove
        self.inLove = inLove
        self.livedYears = 0
        self.lovedYears = 0
        
    def tryToFindLove(self) -> None:
        randomNumber = uniform(0,1)
        if (randomNumber < self.chanceToFindLove):
            self.inLove = True

    def tryToKeepLove(self) -> None:
        randomNumber = uniform(0,1)
        if (randomNumber < self.chanceToLoseLoce):
            self.inLove = False

    def liveYear(self) -> None:
        if (self.isInLove):
            self.tryToKeepLove()
            self.tryToFindLove()
        else:
            self.tryToFindLove()
        self.livedYears += 1
        self.lovedYears += self.inLove

    def isInLove(self) -> bool:
        return self.inLove
    
    def hasNeverLoved(self) -> bool:
        return self.lovedYears == 0;