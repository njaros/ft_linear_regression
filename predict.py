from utils.linearRegressionLib import scaleX, rescaleY, estimatePrice
import sys

def predict(inputFile: str):
	norms: list[list[float]] = [[0.0, 0.0], [0.0, 0.0]]
	theta0: float
	theta1: float
	with open(inputFile, 'r') as io:
		strs = io.readlines()
		io.close()
	theta0 = float(strs[0][9:])
	theta1 = float(strs[1][9:])
	norms[0][0] = float(strs[2][7:])
	norms[0][1] = float(strs[3][7:])
	norms[1][0] = float(strs[4][7:])
	norms[1][1] = float(strs[5][7:])
	print(theta0, '\n', theta1, '\n', norms)
	while True:
		try:
			valRead = float(input("Enter a mileage : "))
		except:
			print("exit")
			exit()
		scaledMileage = scaleX(valRead, norms)
		scaledCost = estimatePrice(scaledMileage, theta0, theta1)
		print(f"The estimate cost is {rescaleY(scaledCost, norms)}")
    
if __name__ == "__main__":
    predict(sys.argv[1])
            