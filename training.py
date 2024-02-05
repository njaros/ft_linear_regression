from utils.linearRegressionLib import *
from utils.myFileManager import MyCSVParser
import json
import matplotlib.pyplot as plt
import sys

def training():
    """training function
    
        This function will creates two "trained" float theta0 and theta1
        which is an estimation of the linear regression of the dataset.
        Those theta0 and theta1 are stocked in the file "thetas" which is used
        by the prediction program to give an estimation to the user
        Complexity  = O(i * O(gradientDescent))
                    = O(i * n) where i = iteration of training, n = length of the dataset
    """
    data = MyCSVParser(sys.argv[1])
    listX = []
    listY = []
    for (x, y) in data.content:
        listX.append(x)
        listY.append(y)
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].set_title("raw dataset")
    axs[0, 1].set_title("scaled dataset and linear regression line")
    axs[1, 0].set_title("quadratic cost in function of theta0")
    axs[1, 1].set_title("quadratic cost in function of theta1")
    axs[0, 0].plot(listX, listY, "ob")
    normalisationScalars = []
    thetas = [0.0, 0.0]
    i: int = 1000
    normalisationScalars = min_maxNormalization(data.content)
    while i:
        axs[1, 0].plot(thetas[0], quadCost(thetas[0], thetas[1], data.content), "ob")
        axs[1, 1].plot(thetas[1], quadCost(thetas[0], thetas[1], data.content), "ob")
        gradientDescent(thetas, 1.7, data.content)
        i -= 1
    listX = []
    listY = []
    for (x, y) in data.content:
        listX.append(x)
        listY.append(y)
    axs[0, 1].plot(listX, listY, "ob")
    axs[0, 1].plot([estimatePrice(x, thetas[0], thetas[1]) for x in range(2)])
    with open("thetas_scale_values.json", 'w') as io:
        json.dump({"theta0": thetas[0],
                   "theta1": thetas[1],
                   "min_max_norms": normalisationScalars},
                  io, indent = 4)
        io.close()
    plt.show()

if __name__ == "__main__":
    training()