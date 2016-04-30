from scipy.optimize import curve_fit
import numpy as np
class Fitter:
    def __init__(self, x, y):
        print "Initialize Fitter..."
        self.x = x
        self.y = y
        self.popt = None
        self.pcov = None

    def fitSinus(self):

        x = np.asarray(self.x)
        y = np.asarray(self.y)

        def sinus(x, a, b, c):
            return a*np.sin(b*x + c)

        print "Compute parameters a,b,c for a * sin(b*x + c)"

        self.popt, self.pcov = curve_fit(sinus, x, y)
        print "Complete!"

    def getParams(self):
        return self.popt