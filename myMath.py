

def add(a: int, b: int) -> int:
    """add function
    
        return a + b
    """
    return a + b

if __name__ == "__main__":
    import sys
    print(add(int(sys.argv[1]), int(sys.argv[2])))