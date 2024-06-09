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
    x = np.random.normal(DISTRIBUTION_MEAN, DISTRIBUTION_SIGMA, NUMBER_OF_LOVERS)
    for chance in x:
        lovers.append(Lover(chance, 0.5))
    for _ in tqdm(range(NUMBER_OF_YEARS_LIVED)):
        for lover in tqdm(lovers):
            lover.liveYear()
    notLoved = []
    for lover in lovers:    
        if (lover.hasNeverLoved()):
            notLoved.append(lover.chanceToFindLove)
    saveResultAsJSON(notLoved)

def saveResultAsJSON(result, name="results.json"):
    saveParams = {
        "numberOfLovers": NUMBER_OF_LOVERS,
        "numberOfYearsLived:": NUMBER_OF_YEARS_LIVED,
        "distributionMean": DISTRIBUTION_MEAN,
        "distributionSigma": DISTRIBUTION_SIGMA,
        "result": result
        }
    with open(name, "w", encoding="utf-8") as file:
        file.write(json.dumps(saveParams))

if __name__ == "__main__":
    if len(sys.argv) == 5:
        NUMBER_OF_YEARS_LIVED = int(sys.argv[1])
        NUMBER_OF_LOVERS = int(sys.argv[2])
        DISTRIBUTION_MEAN = float(sys.argv[3])
        DISTRIBUTION_SIGMA = float(sys.argv[4])
    main()

