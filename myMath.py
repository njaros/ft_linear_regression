

def estimatePrice(mileage: int, theta0: int, theta1:int) -> int:
	"""estimatePrice function

		given a mileage and 2 trained numbers theta0 and theta1,
		this function wille return the estimate price for this mileage
	"""
	return theta0 + theta1 * mileage



def add(a: int, b: int) -> int:
    """add function
    
        return a + b
    """
    return a + b

if __name__ == "__main__":
    import sys
    print(add(int(sys.argv[1]), int(sys.argv[2])))