import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def plot3d(means, sigmas, results):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(means, sigmas, results)
    ax.set_xlabel("Mean")
    ax.set_ylabel("Sigma")

    plt.show()

def contPlot3d(means, sigmas, results):
    x = np.asarray(means)
    y = np.asarray(sigmas)
    X, Y = np.meshgrid(x,y)
    z = np.asarray(results)
    z = z.reshape((len(means), len(sigmas)))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X,Y,z)
    ax.set_xlabel("Mean")
    ax.set_ylabel("Sigma")

    plt.show()