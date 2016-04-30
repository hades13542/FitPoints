import pylab as p


class Plotter:
    def __init__(self, x, y, yafter):
        print(len(x))
        print(len(y))
        p.plot(x, y, '-', x, yafter, '.')
        p.show()




