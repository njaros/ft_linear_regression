from utils.linearRegressionLib import scaleX, rescaleY, estimatePrice
import sys
import json

def predict(inputFile: str):
	try:
		with open(inputFile, 'r') as io:
			jsonData: dict = json.load(io)
			io.close()
		theta0 = jsonData.get("theta0")
		theta1 = jsonData.get("theta1")
		norms = jsonData.get("min_max_norms")
	except:
		print("wrong file input\nexit")
		exit()
	try:
		parsingTrick = estimatePrice(0, theta0, theta1)
		rescaleY(parsingTrick, norms)
	except:
		print("wrong file format\nexit")
		exit()
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
	ac = len(sys.argv)
	if ac == 1:
		print("Need a json file with the thetas values and normalization values\nexit")
		exit()
	predict(sys.argv[1])
            