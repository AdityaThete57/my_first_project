import numpy as np
t = np.linspace(0,10,5)
print(t)
a = np.array([1,2,3])
b = np.array([4,5,6])
v0 = 10
theta = np.pi/4
y0 = 0
g = 9.81
t = np.linspace(0, 2, 100)
print(a+b)
print(np.sqrt(a))
x = v0 + np.sin(theta) * t
y = y0 + v0 * np.cos(theta) * t - 0.5 * g * t**2
print(x)
print(y)