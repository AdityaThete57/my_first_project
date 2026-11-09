import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y,'r--')#r-- means red dashed line, bo means blue circle, g means green line, etc
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis([0, 6, 0, 12]) #set the x and y axis limits
plt.show()
t = np.linspace(0,100,5)
print(t)#0,25,50,75,100
p = range(0, 100, 5)
print(p) #0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95 but doesnt print 100
a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4, 6, 8, 10])
print(a ** b)
print( a % b)#what does this do? It calculates the element-wise modulus of array a by array b, returning the remainder of each division.
print(np.sqrt(a)) #calculates and prints the square root of each element in array a
#old way- for each element, do this operation 
#new way- apply this operation to the whole array
v0 = 50
theta = np.pi / 4  # 45 degrees in radians
g = 9.81  # acceleration due to gravity in m/s^2
t_flight = 2 * v0 * np.sin(theta) / g  # time of flight
t = np.linspace(0, t_flight, 100)  # time from 0 to 10 seconds
x = v0 + np.cos(theta) * t
y = v0 + np.sin(theta) * t - 0.5 * g * t**2
projectile = 2 * v0 * np.sin(theta) / g  # time of flight
plt.plot(x, y, 'r--')
plt.title('Projectile Motion')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.xlim(0, 10) 
plt.ylim(0, 10)
plt.axhline(0, color='blue', lw=0.5)  # Draw a horizontal line at y=0
plt.axvline(0, color='black', lw=0.5)  # Draw a vertical line at x=0
plt.grid()
plt.axis('equal')#plt.axis('off') hides both axis entirely
print(f"Time of flight: {t_flight:.2f} seconds")
print(f"Maximum height: {y.max():.2f} meters")
print(f"Range: {x[-1]:.2f} meters")
plt.show()