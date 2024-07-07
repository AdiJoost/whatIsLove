import numpy as np
from utils.plotter3d import contPlot3d

def main():
    means = np.load("means.npy")
    results = np.load("results.npy")
    sigmas = np.load("sigmas.npy")
    contPlot3d(means, sigmas, results)
    
if __name__ == "__main__":
    main()