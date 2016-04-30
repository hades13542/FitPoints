from SinusGenerator import *
from Fitter import *
from Plotter import *

print "Program initialized"
app = SinusGenerator(0, 9.0, 0.5, 1000)
app.generateSinus()
app.addNoise()
fitter = Fitter(app.getX(), app.getY())
fitter.fitSinus()
app.setParams(fitter.getParams())
app.generateSinusWithParams()
plot = Plotter(app.getX(), app.getYAfterHit(), app.getY())
print "Thanks for using!"
