import numpy as np
from utils.lover import Lover
import json
import sys
from tqdm import tqdm
from utils.plotter3d import plot3d, contPlot3d

NUMBER_OF_SIGMAS = 20
NUMBER_OF_MEANS = 20
TARGET_YEAR = 10
NUMBER_OF_YEARS_LIVED=12
NUMBER_OF_LOVERS=20

def main():
    sigmas = np.linspace(0,1,NUMBER_OF_SIGMAS)
    means = np.linspace(0,1,NUMBER_OF_MEANS)
    results = []
    resultMeans = []
    resultSigmas = []
    for sigma in sigmas:
        for mean in means:
            result = runTargetSimulation(mean, sigma, targetYear=TARGET_YEAR, numbersOfYears=NUMBER_OF_YEARS_LIVED, numbersOfLovers=NUMBER_OF_LOVERS)
            results.append(result)
            resultMeans.append(mean)
            resultSigmas.append(sigma)
    saveResults(means, sigmas, results)
    #contPlot3d(means, sigmas, results)

def saveResults(means, sigmas, results):
    resultsAsArray = np.asarray(results)
    np.save("sigmas.npy", sigmas)
    np.save("means.npy", means)
    np.save("results.npy", resultsAsArray)

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
    if len(sys.argv) == 6:
        NUMBER_OF_SIGMAS = int(sys.argv[1])
        NUMBER_OF_MEANS = int(sys.argv[2])
        TARGET_YEAR = int(sys.argv[3])
        NUMBER_OF_YEARS_LIVED= int(sys.argv[4])
        NUMBER_OF_LOVERS = int(sys.argv[5])
    main()

