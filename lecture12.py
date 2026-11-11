import numpy as np
import matplotlib.pyplot as plt
strain = np.array([0.000,0.001,0.002,0.003,0.004])
stress = np.array([0.0, 20.0, 40.0, 60.0, 80.0])
slope, intercept = np.polyfit(strain, stress, 1)
print(f"Slope = {slope:.2f}")
print(f"Intercept = {intercept:.4f}")
#slope is the young's modulus of the material, and intercept is the stress at zero strain.
E_Pa = slope * 1e6  # Convert from MPa to Pa
E_GPa = E_Pa / 1e9  # Convert from Pa to GPa
print(f"E = {E_Pa:.0f} MPa = {E_GPa:.1f} GPa")

p = 1000
g = 9.81
h = np.linspace(0, 10, 100)
v = np.sqrt(2 * g * h)
pressure_bottom = p * g * h
print('The outlet velocity of the tank is ', v)
print('The pressure at the bottom of the cylindrical tank is: ', pressure_bottom)

plt.plot(h,v, 'r--')
plt.xlabel('height of the tank')
plt.ylabel('outlet velocity')
plt.show()
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,4))#1,2 means 1 row and 2 columns
#fig, axes = plt.subplots(2,2, figsize=(10.8))
ax1.plot(h,v, 'r--')
ax1.set_xlabel('height of the tank')
ax1.set_ylabel('outlet velocity')
ax1.set_title('Toricelli velocity')
ax1.grid(True)

ax2.plot(h,pressure_bottom, 'b--')
ax2.set_xlabel('height of the tank')
ax2.set_ylabel('pressure at the bottom of the tank')
ax2.set_title('Pressure at the bottom of the tank')
ax2.grid(True)
plt.tight_layout()
plt.show()
