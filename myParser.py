import csv

class MyParser:
    def __init__(self, file: str):
        self.fileName = file
        self.content = []
        with open(self.fileName, 'r', newline='') as io:
            self.csvparsing = list(csv.reader(io))
            self.content = [[int(x), int(y)] for (x, y) in self.csvparsing[1:]]
            io.close()

if __name__ == "__main__":
    import sys
    mp = MyParser(str(sys.argv[1]))
    if (mp.content):
        print(mp.content)
    else:
        print("an error occured with fileName = " + mp.fileName)
    
