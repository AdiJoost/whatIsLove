import numpy as np
from utils.lover import Lover
import json
import sys
from tqdm import tqdm

NUMBER_OF_YEARS_LIVED = 10
NUMBER_OF_LOVERS = 20
DISTRIBUTION_MEAN = 0.5
DISTRIBUTION_SIGMA = 0.3


def main():
    lovers = []
    timeEvolution = []
    x = np.random.normal(DISTRIBUTION_MEAN, DISTRIBUTION_SIGMA, NUMBER_OF_LOVERS)
    for chance in x:
        lovers.append(Lover(chance, 0.5))
    for _ in tqdm(range(NUMBER_OF_YEARS_LIVED)):
        countNotLovers = 0
        for lover in tqdm(lovers):
            lover.liveYear()
            if (lover.hasNeverLoved()):
                countNotLovers += 1
        timeEvolution.append(countNotLovers)
    notLovedChances = []
    for lover in lovers:    
        if (lover.hasNeverLoved()):
            notLovedChances.append(lover.chanceToFindLove)
    relativeChange = getRelativeChange(timeEvolution)
    saveResultAsJSON(notLovedChances, timeEvolution, relativeChange)

def saveResultAsJSON(notLovedChances, timeEvolution, relativeChange, name="results.json"):
    saveParams = {
        "numberOfLovers": NUMBER_OF_LOVERS,
        "numberOfYearsLived:": NUMBER_OF_YEARS_LIVED,
        "distributionMean": DISTRIBUTION_MEAN,
        "distributionSigma": DISTRIBUTION_SIGMA,
        "notLovedChances": notLovedChances,
        "timeEvolution": timeEvolution,
        "relativeChange": relativeChange,
        }
    with open(name, "w", encoding="utf-8") as file:
        file.write(json.dumps(saveParams))

def getRelativeChange(timeEvolution) -> list:
    returnList = []
    returnList.append(timeEvolution[0] / float(NUMBER_OF_LOVERS))
    for i in range(1, len(timeEvolution)):
        returnList.append((timeEvolution[i - 1] - timeEvolution[i] )/ float(timeEvolution[i - 1]))
    return returnList    

if __name__ == "__main__":
    if len(sys.argv) == 5:
        NUMBER_OF_YEARS_LIVED = int(sys.argv[1])
        NUMBER_OF_LOVERS = int(sys.argv[2])
        DISTRIBUTION_MEAN = float(sys.argv[3])
        DISTRIBUTION_SIGMA = float(sys.argv[4])
    main()

