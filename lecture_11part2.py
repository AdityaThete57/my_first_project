import matplotlib.pyplot as plt
import numpy as np
import math

x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y)
plt.show()


errors = [404, 500, 404, 302, 500, 200, 404]
unique = set(errors)
print(len(unique))

#Where should the try / except block be placed to process a file that may contain occasional bad rows? 
print(math.tan(math.radians(30)))
print(math.tan(math.degrees(30)))

v0 = 50
theta = np.radians(45)
g = 9.81
t_flight = 2 * v0 * np.sin(theta) / g
print(t_flight)
t = np.linspace(0, t_flight, num=100) #what does this do? It creates an array of 100 evenly spaced values between 0 and t_flight, which can be used to calculate the position of the projectile at different times during its flight.
print(t)