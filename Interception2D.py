import numpy as np
import matplotlib.pyplot as plt
import random
from random import Random

def plot_vector_x_v(x, v):
    l = np.linspace(-10,10)
    xy1 = x[0] + l * v[0]
    xy2 = x[1] + l * v[1]
    plt.plot(xy1, xy2, label = f'{x} + h * {v}')
    plt.plot(x[0], x[1], 'o')

def show_plot():
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axvline(0, linestyle = 'dotted', color = 'k')
    plt.axhline(0, linestyle = 'dotted', color = 'k')
    plt.legend()
    plt.show()
    
def intersection(x1, v1, x2, v2):
    h = ((x1[1]-x2[1]) * v2[0]- (x1[0]-x2[0]) * v2[1])/(v1[0]*v2[1] - v1[1]*v2[0])
    X, Y = x1 + h * v1
    plt.plot(X, Y, 'ok', label = 'intercept')



def main():
    print('Calculate the Interception of two 2D vectors:\n')

    x1 = np.array([0,0])
    x2 = np.array([1,2])
    v1 = np.array([1, 4])
    v2 = np.array([1,-0.6])

    g = Random(28)
    d = 1
    for i in range(4):

        x1 = np.array([g.gauss(0, 1), g.gauss(0, 1)])
        x2 = np.array([g.gauss(0, 1), g.gauss(0, 1)])
        v1 = np.array([g.gauss(0, 1), g.gauss(0, 1)])
        v2 = np.array([g.gauss(0, 1), g.gauss(0, 1)])


        plot_vector_x_v(x1, v1)
        plot_vector_x_v(x2, v2)
        intersection(x1, v1, x2, v2)

        show_plot()





if __name__ == '__main__':
    main()