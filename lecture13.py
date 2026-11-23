class Resistor:# A class to represent a resistor
    def __init__(self, resistance_ohms):# Initialize the resistor with a given resistance, self is the instance of the class
        self.R = resistance_ohms # Resistance in ohms. .R means the resistance of the resistor in ohms. It is a property of the resistor object.
    def current(self, voltage_volts):# Calculate the current through the resistor given a voltage
        return voltage_volts / self.R # Ohm's Law: I = V / R. This method returns the current in amperes when a voltage is applied across the resistor.
def power(self, voltage_volts):# Calculate the power dissipated by the resistor given a voltage
    return voltage_volts * self.current(voltage_volts) # Power P = V * I. This function calculates the power in watts dissipated by the resistor when a voltage is applied across it.
r1 = Resistor(100) # Create a resistor object with 100 ohms resistance
V = 10 # Voltage in volts
print('Resistor resistance:', r1.R, 'ohms') # Print the resistance of the resistor
print('Voltage applied:', V, 'volts') # Print the voltage applied across the resistor