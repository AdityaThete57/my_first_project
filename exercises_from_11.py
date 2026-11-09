import numpy as np
import matplotlib.pyplot as plt
theta1 = np.radians(30)
theta2 = np.radians(60)
v0 = 50
g = 9.81  # acceleration due to gravity in m/s^2
t_flight1 = 2 * v0 * np.sin(theta1) / g  # time of flight for 30 degrees
t_flight2 = 2 * v0 * np.sin(theta2) / g  # time of flight for 60 degrees
t = np.linspace(0, max(t_flight1, t_flight2), 100)  # time from 0 to max flight time
x = v0 * np.cos(theta1)
y = v0 * np.sin(theta1) - 0.5 * g * t**2
print(f"Projectile motion at 30 degrees: x = {x:.2f} m")

x = v0 * np.cos(theta2)
y = v0 * np.sin(theta2) - 0.5 * g * t**2
print(f"Projectile motion at 60 degrees: x = {x:.2f} m")

plt.plot(x, y)
plt.title('Projectile Motion at 30 and 60 Degrees')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.show()