import math
import numpy as np

theta1 = 0.3
theta2 = -0.1
delta1 = -0.003
delta2 = 0.002
d1 =  0.1
d2 = 0.15

def fk(theta_1, theta_2):
    theta = theta_1 + theta_2
    x = d1*math.cos(theta_1) + d2*math.cos(theta)
    y = d1*math.sin(theta_1) + d2*math.sin(theta)
    return x, y, theta


def J(theta_1, theta_2):
    theta = theta_1 + theta_2
    j = [[0, 0] for _ in range(3)]
    j[0][0] = -d1*math.sin(theta_1) - d2*math.sin(theta)
    j[0][1] = -d2*math.sin(theta)
    j[1][0] = d1*math.cos(theta_1) + d2*math.cos(theta)
    j[1][1] = d2*math.cos(theta)
    j[2][0] = 1
    j[2][1] = 1

    return j

print(fk(theta1, theta2))
print(fk(theta1+delta1, theta2+delta2))
print(J(theta1, theta2))
print(fk(theta1, theta2) + np.dot(J(theta1, theta2), [delta1, delta2]))

