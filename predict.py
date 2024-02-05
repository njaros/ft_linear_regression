from utils.linearRegressionLib import scaleX, rescaleY, estimatePrice
import sys
import json

def predict(inputFile: str):
	with open(inputFile, 'r') as io:
		jsonData: dict = json.load(io)
		io.close()
	theta0 = jsonData.get("theta0")
	theta1 = jsonData.get("theta1")
	norms = jsonData.get("min_max_norms")
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
            