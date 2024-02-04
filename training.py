from utils.linearRegressionLib import *
from utils.myParser import MyParser
import matplotlib.pyplot as plt
import sys

def f(x):
    return 9000 - 0.022 * x

def training():
    """training function
    
        This function will creates two "trained" float theta0 and theta1
        which is an estimation of the linear regression of the dataset.
        Those theta0 and theta1 are stocked in the file "thetas" which is used
        by the prediction program to give an estimation to the user
        Complexity  = O(i * O(gradientDescent))
                    = O(i * n) where i = iteration of training, n = length of the dataset
    """
    data = MyParser(sys.argv[1])
    listX = []
    listY = []
    for (x, y) in data.content:
        listX.append(x)
        listY.append(y)
    fig, axs = plt.subplots(1, 2)
    axs[0].plot(listX, listY, "ob")
    normalisationScalars = []
    thetas = [0.0, 0.0]
    i: int = 100
    print(data.content)
    normalisationScalars = min_maxNormalization(data.content)
    print(data.content)
    while i:
        gradientDescent(thetas, 1.6, data.content)
        i -= 1
    #rescaleThetas(thetas, normalisationScalars)
    print(f"{thetas=}")
    listX = []
    listY = []
    for (x, y) in data.content:
        listX.append(x)
        listY.append(y)
    #rescaleX(listX, normalisationScalars)
    #rescaleY(listY, normalisationScalars)
    axs[0].plot([f(x) for x in range(250000)])
    axs[1].plot(listX, listY, "ob")
    axs[1].plot([estimatePrice(x, thetas[0], thetas[1]) for x in range(0, 2)])
    plt.show()
    
if __name__ == "__main__":
    training()