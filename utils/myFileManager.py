import csv

class MyCSVParser:
    def __init__(self, file: str):
        self.fileName: str = file
        self.content: list[list[float]] = [[], []]
        with open(self.fileName, 'r', newline='') as io:
            self.csvparsing = list(csv.reader(io))
            for (x, y) in self.csvparsing[1:]:
                self.content[0].append(float(x))
                self.content[1].append(float(y))
            io.close()

if __name__ == "__main__":
    import sys
    mp = MyCSVParser(str(sys.argv[1]))
    if (mp.content):
        print(mp.content)
    else:
        print("an error occured with fileName = " + mp.fileName)
