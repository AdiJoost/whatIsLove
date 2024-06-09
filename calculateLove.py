import numpy as np
from utils.lover import Lover
import json

NUMBER_OF_SAME_LOVERS = 3
NUMBER_OF_YEARS_LIVED = 10

def main():
    lovers = []
    x = np.linspace(0.01,1,20)
    for chance in x:
        for _ in range(NUMBER_OF_SAME_LOVERS):
            lovers.append(Lover(chance, 20))
    for _ in range(NUMBER_OF_YEARS_LIVED):
        for lover in lovers:
            lover.liveYear()
    notLoved = []
    for lover in lovers:    
        if (lover.hasNeverLoved()):
            notLoved.append(lover.chanceToFindLove)
    saveResultAsJSON(notLoved)

def saveResultAsJSON(result, name="results.json"):
    with open(name, "w", encoding="utf-8") as file:
        file.write(json.dumps(result))

if __name__ == "__main__":
    main()

