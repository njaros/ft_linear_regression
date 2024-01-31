from myMath import add
import myMath
import sys

def main():
    for i in dir(myMath):
        print(i)    
    print(add(1, 3))

if __name__ == "__main__":
    main()