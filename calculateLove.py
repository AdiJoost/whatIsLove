import numpy as np
from utils.lover import Lover
import json
import sys

NUMBER_OF_SAME_LOVERS = 3
NUMBER_OF_YEARS_LIVED = 10
NUMBER_OF_DIFFERENT_LOVERS = 20

def main():
    lovers = []
    x = np.linspace(0.01,1,NUMBER_OF_DIFFERENT_LOVERS)
    for chance in x:
        for _ in range(NUMBER_OF_SAME_LOVERS):
            lovers.append(Lover(chance, 0.5))
    for _ in range(NUMBER_OF_YEARS_LIVED):
        for lover in lovers:
            lover.liveYear()
    notLoved = []
    for lover in lovers:    
        if (lover.hasNeverLoved()):
            notLoved.append(lover.chanceToFindLove)
    saveResultAsJSON(notLoved)

def saveResultAsJSON(result, name="results.json"):
    saveParams = {"numberOfSameLovers": NUMBER_OF_SAME_LOVERS,
     "numberOfYearsLived:": NUMBER_OF_YEARS_LIVED,
     "numberOfDifferentLovers": NUMBER_OF_DIFFERENT_LOVERS,
     "result": result}
    with open(name, "w", encoding="utf-8") as file:
        file.write(json.dumps(saveParams))

if __name__ == "__main__":
    if len(sys.argv) == 4:
        NUMBER_OF_SAME_LOVERS = int(sys.argv[1])
        NUMBER_OF_YEARS_LIVED = int(sys.argv[2])
        NUMBER_OF_DIFFERENT_LOVERS = int(sys.argv[3])
    main()

