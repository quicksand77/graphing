__author__ = 'quicksand77'
import matplotlib.pyplot as plot
class DataPlot:
    def __init__(self):
        self.path = 'randtemp.txt'
        self.x = []
        self.y = []
    def doStuff(self):
        with open(self.path,'r') as readFile:
            sepFile = readFile.read().split('\n')
        for plotPair in sepFile:
            xAndY = plotPair.split(',')
            self.x.append(int(xAndY[0]))
            self.y.append(int(xAndY[1]))