from utils.linearRegressionLib import min_maxNormalization, estimatePrice, quadCost, gradientDescent
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
        quadCostVal = quadCost(thetas[0], thetas[1], dataSet)
        axs[1, 0].plot(thetas[0], quadCostVal, "ob")
        axs[1, 1].plot(thetas[1], quadCostVal, "ob")
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
    axs[1, 2].legend()
    plt.show()

if __name__ == "__main__":
    ac = len(sys.argv)
    if ac == 1:
        print("need a csv file as first argument\nexit")
        exit()
    try:
        csvData = MyCSVParser(sys.argv[1]).content
    except:
        print("wrong file input\nexit")
        exit()
    if ac > 2:
        try:
            learningRate = float(sys.argv[2])
        except:
            print("couldn't cast the learningRate entry as a float, value set to 1")
            learningRate = 1
    else:
        print("no entry for learningRate, value set to 1")
        learningRate = 1
    if ac > 3:
        try:
            iterations = int(sys.argv[3])
        except:
            print("couldn't cast the iterations entry as an int, value set to 100")
            iterations = 100
    else:
        print("no entry for iterations, value set to 100")
        iterations = 100
    training(csvData, learningRate, iterations)