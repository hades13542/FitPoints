import math
import random


class SinusGenerator:
    def __init__(self, x_min, x_max, noise=0, samples=20):
        print "Sinus generator initialized"
        self._noise = noise
        self._xmin = x_min
        self._xmax = x_max
        self._samples = samples
        self.x = None
        self.y = None
        self.yAfterFit = []
        self.params = None

    def generateSinus(self):
        print "Generate sinus function"
        delta = self._xmax / self._samples
        self.x = [delta * i for i in range(0, self._samples + 1)]
        self.y = [math.sin(j) for j in self.x]

    def generateSinusWithParams(self):
        for i in self.x:
            y_value = self.params[0] * math.sin(self.params[1] * i + self.params[2])
            self.yAfterFit.append(y_value)

    def getX(self):
        return self.x

    def setParams(self,params):
        self.params = params

    def getY(self):
        return self.y

    def getYAfterHit(self):
        return self.yAfterFit

    def addNoise(self):
        print "Adding noise to function"
        self.y = [i + random.uniform(-self._noise, self._noise) for i in self.y]

    def saveFileToTest(self):
        f = open('result.dat', 'w')
        for i in range(0, self._samples + 1):
            f.write('{0} \t {1} \n'.format(self.x[i], self.y[i]))
        f.close()
