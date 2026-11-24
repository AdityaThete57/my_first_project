import math
class Resistor:# A class to represent a resistor (The whole circuit)
    #what attributes and methods does a resistor have? A resistor has a resistance value (in ohms) and can calculate the current through it given a voltage, as well as the power dissipated given a voltage.

    def __init__(self, resistance_ohms):# Initialize the resistor with a given resistance, self is the name given to the resistor object being created. It is a reference to the instance of the class.
        self.R = resistance_ohms # .R is like a small box inside self that holds the value of the resistance in ohms. It is an attribute of the resistor object.
    def current(self, voltage_volts):# Calculate the current through the resistor given a voltage
        return voltage_volts / self.R # Ohm's Law: I = V / R. This method returns the current in amperes when a voltage is applied across the resistor.
    def power(self, voltage_volts):# Calculate the power dissipated by the resistor given a voltage
        return voltage_volts * self.current(voltage_volts) # Power P = V * I. This function calculates the power in watts dissipated by the resistor when a voltage is applied across it.

r1 = Resistor(100) # Create a resistor object with 100 ohms resistance, thus self.R will be 100 ohms.
V = 10 # Voltage in volts
I = r1.current(V) # Calculate the current through the resistor using the current method,
#why r1.current instead of current(r1, V)? Because current is a method of the Resistor class, and we call it on the instance r1. The method takes the voltage as an argument and uses the resistance of r1 to calculate the current.
P = r1.power(V) # Calculate the power dissipated by the resistor using the power method
print('Resistor resistance:', r1.R, 'ohms') # Print the resistance of the resistor
print('Voltage applied:', V, 'volts') # Print the voltage applied across the resistor
print('Current through the resistor:', I, 'amperes') # Print the current through the resistor
print('Power dissipated by the resistor:', P, 'watts') # Print the power dissipated by the resistor

class Thermistor(Resistor):
    # A class to represent a thermistor, which is a type of resistor whose resistance changes with temperature. It inherits from the Resistor class.
    def __init__(self,resistance_ohms,A=0.001,B=0.0002):#Reuses everything found in the parent constructor insead of writing self.R again or method of current again
        super().__init__(resistance_ohms) # Call the constructor of the parent Resistor class to initialize the resistance
        self.A = A # Coefficient A for the temperature-resistance relationship
        self.B = B # Coefficient B for the temperature-resistance relationship
    def temperature(self):
        # Calculate the temperature based on the resistance using the Steinhart-Hart equation or a simplified version
        return(1.0/(self.A + self.B * math.log(self.R))) # This method calculates the temperature in Kelvin based on the resistance of the thermistor using a logarithmic relationship.
therm = Thermistor(1000) # Create a thermistor object with 1000 ohms resistance
print(f'Temperature: {therm.temperature():.2f} K') # Print the calculated temperature in Kelvin
print(f'Current @ 5V: {therm.current(5):.4f} A') # Print the current through the thermistor when 5 volts is applied
    