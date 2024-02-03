

def estimatePrice(mileage: int, theta0: int, theta1: int) -> int:
	"""estimatePrice function

		given a mileage and 2 trained numbers theta0 and theta1,
		this function wille return the estimate price for this mileage
	"""
	return theta0 + theta1 * mileage

def quadCost(theta0: float, theta1: float, data) -> float:
    """quadratique cost function
      
		This function return the average of the sum of the error between the
        equation line y = theta0 + theta1 * x and the data for each (x, y) couple in the data
    """
    quadErrorSum = 0
    for (x, y) in data:
        quadErrorSum += (estimatePrice(x, theta0, theta1) - y)**2
    return quadErrorSum / (2 * len(data))

def gradientLC(theta0: float, theta1: float, data) -> float:
	"""gradient of the leading coefficient theta1

		this function return the direction of the slope of the deritative of the curve
        of the quadCost as function of Theta1 for the given parameters theta0 and theta1
	""" 
	errorSum = 0
	for (x, y) in data:
		errorSum += (estimatePrice(x, theta0, theta1) - y) * x
	return errorSum / len(data)

def gradientOrigin(theta0: float, theta1: float, data) -> float:
	"""gradient of the origin theta0

		this function return the direction of the slope of the deritative of the curve
		of the quadCost as function of Theta0 for the given parameters theta0 and theta1
	"""
	errorSum = 0
	for (x, y) in data:
		errorSum += estimatePrice(x, theta0, theta1) - y
	return errorSum / len(data)

def gradientDescent(theta0: float, theta1: float, learningRate: float, data) -> (float, float):
	"""Descent of gradient function
	
		given a theta0, theta1, learningRate and a dataset, this function will creates new parameters newTheta0 and newTheta1
		which are respectively equal to theta0 - learningRate * gradientOrigin and theta1 - learningRate * gradientLC.
		Thoses value are supposed to be better components of the linear regression of the data,
		having for equation line y = theta1 * x + theta0
	"""
	newTheta0 = theta0 - (learningRate * gradientOrigin(theta0, theta1, data))
	newTheta1 = theta1 - (learningRate * gradientLC(theta0, theta1, data))
	return (newTheta0, newTheta1)
