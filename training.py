from utils.linearRegressionLib import *
from utils.myFileManager import MyCSVParser
import json
import matplotlib.pyplot as plt
import sys

def prepareSubplots(learningRate, iterations):
    fig, axs = plt.subplots(2, 3)
    fig.suptitle(f"{learningRate=}, {iterations=}")
    axs[0, 0].set_title("raw dataset")
    axs[0, 1].set_title("scaled dataset and linear regression line")
    axs[0, 2].set_title("evolution of the linear regression line")
    axs[1, 0].set_title("quadratic cost in function of theta0")
    axs[1, 1].set_title("quadratic cost in function of theta1")
    axs[1, 2].set_title("evolution of theta0 and theta1")
    return axs

def training(dataSet, learningRate, iterations):
    """training function
    
        This function will creates two "trained" float theta0 and theta1
        which is an estimation of the linear regression of the dataset.
        Those theta0 and theta1 are stocked in the file "thetas" which is used
        by the prediction program to give an estimation to the user.
        Some graphics will be drawed to take a look of the algorithm works.
        Complexity  = O(i * O(gradientDescent))
                    = O(i * n) where i = iteration of training, n = length of the dataset
    """
    axs = prepareSubplots(learningRate, iterations)
    axs[0, 0].plot(dataSet[0], dataSet[1], "ob")
    normalisationScalars = min_maxNormalization(dataSet)
    axs[0, 1].plot(dataSet[0], dataSet[1], "ob")
    thetas = [0.0, 0.0]
    thetasCurve = []
    thetasCurve.append(tuple(thetas))
    axs[0, 2].plot([estimatePrice(x, thetas[0], thetas[1]) for x in range(2)])
    
    for i in range(iterations):
        axs[1, 0].plot(thetas[0], quadCost(thetas[0], thetas[1], dataSet), "ob")
        axs[1, 1].plot(thetas[1], quadCost(thetas[0], thetas[1], dataSet), "ob")
        gradientDescent(thetas, learningRate, dataSet)
        axs[0, 2].plot([estimatePrice(x, thetas[0], thetas[1]) for x in range(2)])
        thetasCurve.append(tuple(thetas))
        
    axs[1, 2].plot([thetasCurve[i][0] for i in range(len(thetasCurve))], "r", label="theta0")
    axs[1, 2].plot([thetasCurve[i][1] for i in range(len(thetasCurve))], "g", label="theta1")
    axs[0, 1].plot([estimatePrice(x, thetas[0], thetas[1]) for x in range(2)])
    
    with open("thetas_scale_values.json", 'w') as io:
        json.dump({"theta0": thetas[0],
                   "theta1": thetas[1],
                   "min_max_norms": normalisationScalars},
                  io, indent = 4)
        io.close()
    axs[0, 2].legend()
    plt.show()

if __name__ == "__main__":
    learningRate = 1
    iterations = 100
    try:
        csvData = MyCSVParser(sys.argv[1]).content
    except:
        print("wrong file input")
        exit()
    try:
        learningRate = float(sys.argv[2])
        iterations = int(sys.argv[3])
    finally:
        training(csvData, learningRate, iterations)