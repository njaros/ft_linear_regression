
def min_maxNormalization(data: list[list[float]]) -> tuple[tuple[float, float], tuple[float, float]]:
    """data normalization function
	
        given a dataset data with 2 columns, this function will move all data
        to get all minimum to 0, then divide all elements in the first column
        by the max of this column. Same for the second column.
	    Then it will return the x diviser and the y diviser.
        Complexity  = (8 + 4 + 2 + 4 * complexity(max or min)) * n + 2
                    = (12 + 4 * O(1)) * n + 2
                    = O(n) where n = length of dataset
	"""
    maxX: float = data[0][0]
    minX: float = data[0][0]
    maxY: float = data[1][0]
    minY: float = data[1][0]
    
    for x in data[0]:
        minX = min(minX, x)
        maxX = max(maxX, x)
    for y in data[1]:
        minY = min(minY, y)
        maxY = max(maxY, y)
    for i in range(len(data[0])):
        data[0][i] = (data[0][i] - minX) / (maxX - minX)
        data[1][i] = (data[1][i] - minY) / (maxY - minY)
    return ((minX, maxX), (minY, maxY))

def scaleX(mileage: float, norms) -> float:
	"""create a scaled value from a mileage to have sense with scaled trained thetas values

		mileage : a float
		norms : the datas registered to normalize or denormalize
	"""
	scaledX = (mileage - norms[0][0]) / (norms[0][1] - norms[0][0])
	return scaledX
        
def rescaleY(scaledCost: float, norms) -> float:
	"""rescale a result value from the linear regression formula to give a readable value to the user
 
		scaledCost : a float
		norms : the datas registered to normalize or denormalize
	"""
	readableCost = (scaledCost * (norms[1][1] - norms[1][0])) + norms[1][0]
	return readableCost

def estimatePrice(mileage: float, theta0: float, theta1: float) -> float:
	"""estimatePrice function

		given a mileage and 2 trained numbers theta0 and theta1,
		this function wille return the estimate price for this mileage
        Complexity  = 2 (+ *)
                    = O(1)
	"""
	return theta0 + theta1 * mileage

def quadCost(theta0: float, theta1: float, data: list[list[float]]) -> float:
    """quadratique cost function
      
		This function return the average of the sum of the error between the
        equation line y = theta0 + theta1 * x and the data for each (x, y) couple in the data
        Complexity  = 2 (x, y) * n (data) * (2 (+=) + 1 (O(estimatePrice))) + 4 (= * / len)
                    = O(n) where n = length of dataset
    """
    quadErrorSum = 0
    for i in range(len(data[0])):
        quadErrorSum += (estimatePrice(data[0][i], theta0, theta1) - data[1][i])**2
    return quadErrorSum / (2 * len(data[0]))

def gradientLC(theta0: float, theta1: float, data: list[list[float]]) -> float:
	"""gradient of the leading coefficient theta1

		this function return the direction of the slope of the deritative of the curve
        of the quadCost as function of theta1 for the given parameters theta0 and theta1
        Complexity = O(n) where n = length of dataset
	""" 
	errorSum = 0
	for i in range(len(data[0])):
		errorSum += (estimatePrice(data[0][i], theta0, theta1) - data[1][i]) * data[0][i]
	return errorSum / len(data[0])

def gradientOrigin(theta0: float, theta1: float, data: list[list[float]]) -> float:
	"""gradient of the origin theta0

		this function return the direction of the slope of the deritative of the curve
		of the quadCost as function of theta0 for the given parameters theta0 and theta1
        Complexity = O(n) where n = length of dataset
	"""
	errorSum = 0
	for i in range(len(data[0])):
		errorSum += estimatePrice(data[0][i], theta0, theta1) - data[1][i]
	return errorSum / len(data[0])

def gradientDescent(thetas: list[float], learningRate: float, data: list[list[float]]):
	"""Descent of gradient function
	
		given a theta0, theta1, learningRate and a dataset, this function will creates new parameters newTheta0 and newTheta1
		which are respectively equal to theta0 - learningRate * gradientOrigin and theta1 - learningRate * gradientLC.
		Thoses value are supposed to be better components of the linear regression of the data,
		having for equation line y = theta1 * x + theta0
        Complexity  = Complexity of gradientOrigin + Complexity of gradientLC
                    = O(n) + O(n)
                    = O(n) where n = length of dataset
	"""
	newTheta0 = thetas[0] - (learningRate * gradientOrigin(thetas[0], thetas[1], data))
	newTheta1 = thetas[1] - (learningRate * gradientLC(thetas[0], thetas[1], data))
	thetas[0] = newTheta0
	thetas[1] = newTheta1
