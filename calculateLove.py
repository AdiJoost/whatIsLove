import numpy as np
from utils.lover import Lover
import json
import sys
from tqdm import tqdm
from utils.plotter3d import plot3d, contPlot3d

NUMBER_OF_YEARS_LIVED = 10
NUMBER_OF_LOVERS = 200
DISTRIBUTION_MEAN = 0.5
DISTRIBUTION_SIGMA = 0.3

def main():
    sigmas = np.linspace(0,1,20)
    means = np.linspace(0,1,20)
    results = []
    resultMeans = []
    resultSigmas = []
    for sigma in sigmas:
        for mean in means:
            result = runTargetSimulation(mean, sigma, numbersOfLovers=20)
            results.append(result)
            resultMeans.append(mean)
            resultSigmas.append(sigma)
    saveResults(means, sigmas, results)
    contPlot3d(means, sigmas, results)

def saveResults(means, sigmas, results):
    resultsAsArray = np.asarray(results)
    np.save("sigmas.npy", sigmas)
    np.save("means.npy", means)
    np.save("results.npy", resultsAsArray)
    

def runNormalSimulation():
    lovers = []
    timeEvolution = []
    notLovedChances = []
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
#    for lover in lovers:    
#        if (lover.hasNeverLoved()):
#            notLovedChances.append(lover.getLoverChance())
    relativeChange = getRelativeChange(timeEvolution)
    saveResultAsJSON(notLovedChances, timeEvolution, relativeChange)

def runTargetSimulation(mean, sigma, targetYear=10, numbersOfYears=12, numbersOfLovers=10000):
    lovers = []
    timeEvolution = []
    notLovedChances = []
    x = np.random.normal(mean, sigma, numbersOfLovers)
    for chance in x:
        lovers.append(Lover(chance, 0.5))
    for _ in tqdm(range(numbersOfYears)):
        countNotLovers = 0
        for lover in tqdm(lovers):
            lover.liveYear()
            if (lover.hasNeverLoved()):
                countNotLovers += 1
        timeEvolution.append(countNotLovers)
    for lover in lovers:    
        if (lover.hasNeverLoved()):
            notLovedChances.append(lover.getLoverChance())
    relativeChange = getRelativeChange(timeEvolution)
    return relativeChange[targetYear]


def saveResultAsJSON(notLovedChances, timeEvolution, relativeChange: np.ndarray, name="results.json"):
    saveParams = {
        "numberOfLovers": NUMBER_OF_LOVERS,
        "numberOfYearsLived:": NUMBER_OF_YEARS_LIVED,
        "distributionMean": DISTRIBUTION_MEAN,
        "distributionSigma": DISTRIBUTION_SIGMA,
        "notLovedChances": notLovedChances,
        "timeEvolution": timeEvolution,
        "relativeChange": relativeChange.tolist(),
        }
    with open(name, "w", encoding="utf-8") as file:
        file.write(json.dumps(saveParams))

def getRelativeChange(timeEvolution) -> list:
    returnList = np.zeros(len(timeEvolution))
    returnList[0] = (timeEvolution[0] / float(NUMBER_OF_LOVERS))
    for i in range(1, len(timeEvolution)):
        if (float(timeEvolution[i-1]) != 0):
            returnList[i] = ((timeEvolution[i - 1] - timeEvolution[i] )/ float(timeEvolution[i - 1]))
        else:
            returnList[i] = 0
        if timeEvolution == 0:
            break
    return returnList    

if __name__ == "__main__":
    if len(sys.argv) == 5:
        NUMBER_OF_YEARS_LIVED = int(sys.argv[1])
        NUMBER_OF_LOVERS = int(sys.argv[2])
        DISTRIBUTION_MEAN = float(sys.argv[3])
        DISTRIBUTION_SIGMA = float(sys.argv[4])
    main()

