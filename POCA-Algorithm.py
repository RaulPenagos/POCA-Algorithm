"""
Minimum Distance 3D

This script defines functions to get the POCA of 3D lines
In case two 3d lines are not parallel or do intercept, their POCA
is their point of closest approach between the two. 

The script includes functions to plot 3D lines, find their POCA, or 
find and plot their POCA.

Functions:
    plot_line_3D(x, v, range)
    POCA_algorithm(xa, va, xb, vb)
    find_closest_point(xa, va, xb, vb)

@author Raúl Penagos
@date   April 14th, 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d



def plot_line_3D(x, v, range: float = 5):
    """
    Given a point and vector of a 3D line, it creates its plot for a range of desire
    """
    #  
    min = -range
    max = range
    x_min, y_min, z_min = x + min*v
    x_max, y_max, z_max = x + max*v
    graf_3D.plot([x_min, x_max], [y_min, y_max], [z_min, z_max])


def POCA_algorithm(xa, va, xb, vb):
    """
    Given two D-space lines, defined by a point (x) and vector (v) 
    Finds the POCA and returns True and its value as a tuple [x,y,z]
    In case the two lines are parallel, it returns False and (0,0,0)
    """
    d = xa - xb

    A = np.dot(d , va)
    B = np.dot(va, va) 
    C = np.dot(va, vb)
    D = np.dot(d , vb) 
    E = np.dot(vb, vb)

    denominator = B*E - C**2

    if denominator == 0:
        return False, [0,0,0]

    alpha = (D*C - A*E) / denominator 
    beta =  (D*B - A*C) / denominator

    P_a = xa + alpha * va
    P_b = xb + beta * vb

    POCA = (P_a + P_b)/2

    return True, [POCA[0],POCA[1],POCA[2]]


def find_closest_point(xa, va, xb, vb):
    """
    Given two D-space lines, defined by a point (x) and vector (v) 
    Finds the POCA and returns True and its value as a tuple [x,y,z]
    In case the two lines are parallel, it returns False and (0,0,0)

    It also plots the POCA as a point and segment between the two lines
    """

    d = xa - xb

    A = np.dot(d , va)
    B = np.dot(va, va) 
    C = np.dot(va, vb)
    D = np.dot(d , vb) 
    E = np.dot(vb, vb)
    # F = C

    denominator = B*E - C**2

    if denominator == 0:
        print('Rectas paralelas') 

    alpha = (D*C - A*E) / denominator 
    beta =  (D*B - A*C) / denominator

    P_a = xa + alpha * va
    P_b = xb + beta * vb

    # graf_3D.plot(P_a[0],P_a[1],P_a[2], 'or')
    # graf_3D.plot(P_b[0],P_b[1],P_b[2], 'or')
    graf_3D.plot([P_a[0], P_b[0]],[P_a[1], P_b[1]],[P_a[2], P_b[2]])
    
    POCA = (P_a + P_b)/2
    graf_3D.plot(POCA[0],POCA[1],POCA[2], 'or')


# TEST////////////////////////////////////////////////////////////////////////

# Create two arbitrary lines
x_a = np.array([0, 0, 0])
# x_a = np.array([1, 1, 1])
v_a = np.array([1, 2, 0.5])
# x_b = np.array([0.6, 0.8, 1])
x_b = np.array([2.5, 0, 1])
v_b = np.array([1, 1, 1])

# Plot 3D
fig_3D = plt.figure()
graf_3D = fig_3D.add_subplot(111, projection='3d')

plot_line_3D(x_a, v_a)
plot_line_3D(x_b, v_b)

# Find and plot POCA
find_closest_point(x_a, v_a, x_b, v_b)

graf_3D.set_title('POCA')
graf_3D.set_xlabel('x')
graf_3D.set_ylabel('y')
graf_3D.set_zlabel('z')
graf_3D.set_xlim([-5,5])
graf_3D.set_ylim([-5,5])
graf_3D.set_zlim([-5,5])
# grafica.legend()
eleva = 30
rota = -45
deltaw = 1
graf_3D.view_init(eleva, rota)

# rotacion de ejes
for angulo in range(rota, 360+rota, deltaw ):
    graf_3D.view_init(eleva, angulo)
    plt.draw()
    plt.pause(.001)
plt.show()
