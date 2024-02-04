import csv

class MyParser:
    def __init__(self, file: str):
        self.fileName: str = file
        self.content: list[list[float]]
        with open(self.fileName, 'r', newline='') as io:
            self.csvparsing = list(csv.reader(io))
            self.content = [[float(x), float(y)] for (x, y) in self.csvparsing[1:]]
            io.close()

if __name__ == "__main__":
    import sys
    mp = MyParser(str(sys.argv[1]))
    if (mp.content):
        print(mp.content)
    else:
        print("an error occured with fileName = " + mp.fileName)
    
