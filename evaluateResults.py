import numpy as np
import json
import matplotlib.pyplot as plt


def main():
    result = _getResult()
    visualizeRelativeChange(result)
    

def visualizeRelativeChange(result):
    plt.plot(result["relativeChange"])
    plt.show()

def visualizeNotLoverChances(result):
    notLovers = result["result"]
    print(len(notLovers))
    print(result["numberOfLovers"])
    data = [x for x in notLovers if x > 0]
    bins = np.arange(0, 1.05, 0.05)
    counts, bin_edges, patches = plt.hist(data, bins=bins, edgecolor='black', density=True)

    print("Bin counts (density):", counts)
    print("Sum of bin counts (density):", np.sum(counts * np.diff(bin_edges)))
    plt.show()


def _getResult():
    with open("results.json", "r", encoding="utf-8") as file:
        return json.loads(file.read())


if __name__ == "__main__":
    main()