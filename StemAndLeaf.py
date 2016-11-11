"""
A simple stem and leaf plot class
"""

class StemAndLeafPlot:
    def __init__(self, numList):
        self.numList = sorted(numList)

    def plot(self):
        numDict = self.constructPlotDict()
        for i in numDict:
            print("{} | ".format(i), end="")
            for j in numDict[i]:
                print("{} ".format(j), end="")
            print("")

        print("\nKey: 1 | 2 = 12")

    def constructPlotDict(self):
        numDict = {}
        highNum = self.numList[-1]
        slots = int(highNum / 10)
        # create all the necessary slots
        for i in range(0, slots+1):
            numDict[i] = []

        # place everything in the right list
        for i in self.numList:
            if i < 10:
                numDict[0].append(i)
            else:
                numStr = str(i)
                numDict[int(numStr[:-1])].append(numStr[-1])
        return numDict

def main():
    numList = [1,1,2,3,3,5,6,7,7,7,7,8,8,9,9,10,10,14,15,15,15,15,15,20,21]
    sal = StemAndLeafPlot(numList)
    sal.plot()

if __name__ == "__main__":
    main()