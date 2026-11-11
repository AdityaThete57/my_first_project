import numpy as np
strain = np.array([0.000,0.001,0.002,0.003,0.004])
stress = np.array([0.0, 20.0, 40.0, 60.0, 80.0])
slope, intercept = np.polyfit(strain, stress, 1)
print(f"Slope = {slope:.2f}")
print(f"Intercept = {intercept:.4f}")
#slope is the young's modulus of the material, and intercept is the stress at zero strain.
E_Pa = slope * 1e6  # Convert from MPa to Pa
E_GPa = E_Pa / 1e9  # Convert from Pa to GPa
print(f"E = {E_Pa:.0f} MPa = {E_GPa:.1f} GPa")