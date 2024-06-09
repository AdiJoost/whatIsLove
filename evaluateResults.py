import numpy as np
import json
import matplotlib.pyplot as plt

def main():
    result = _getResult()
    notLovers = result["result"]
    print(len(notLovers))
    print(result["numberOfLovers"])
    data = [0 if x < 0 else x for x in notLovers]
    bins = np.arange(0, 1.1, 0.1)
    plt.hist(data, bins=bins, edgecolor='black')
    plt.show()


def _getResult():
    with open("results.json", "r", encoding="utf-8") as file:
        return json.loads(file.read())


if __name__ == "__main__":
    main()