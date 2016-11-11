"""
A simple stem and leaf plot class
"""

class StemAndLeafPlot:
    def __init__(self, numList):
        self.numList = sorted(numList)

    def plot(self):
        # The number of digits in the biggest number
        maxDigits = len(str(self.numList[-1]))

        numDict = self.constructPlotDict()
        for i in numDict:
            numLength = len(str(i))
            # Print the stem, the buffer spacing, and a pipe
            print("{}{}| ".format(i, " "*(maxDigits - numLength)), end="")
            for j in numDict[i]:
                # Print all of the leaves for this stem
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
    import random
    numList = []
    for i in range(100):
        numList.append(random.randint(0,100))
    sal = StemAndLeafPlot(numList)
    sal.plot()

if __name__ == "__main__":
    main()
