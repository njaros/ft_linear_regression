from linearRegressionLib import *
from myParser import MyParser
import linearRegressionLib
import sys

def main():
    data = MyParser(sys.argv[1])
    normalisationScalar = []
    thetas = [0, 0]
    i: int = 2000
    print(data.content)
    normalisationScalar = dataNormalization(data.content)
    print(data.content)
    while i:
        thetas = gradientDescent(thetas[0], thetas[1], 1.6, data.content)
        print(thetas[0] * normalisationScalar[0], thetas[1] * normalisationScalar[1])
        i -= 1

if __name__ == "__main__":
    main()