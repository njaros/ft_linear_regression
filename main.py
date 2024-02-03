from linearRegressionLib import *
from myParser import MyParser
import linearRegressionLib
import sys

def main():
    data = MyParser(sys.argv[1])
    thetas = (0, 0)
    i: int = 20
    print(data.content)
    while i:
        thetas = gradientDescent(thetas[0], thetas[1], 0.3, data.content)
        print(thetas)
        i -= 1

if __name__ == "__main__":
    main()