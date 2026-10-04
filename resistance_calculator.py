#To calculate total resistance when random values assigned
import random
test = []
total = 0
for i in range(10):
    resistor = random.randint(100, 1000)
    test.append(resistor)
    total += resistor
print('The resistance values are: ',test)
print(f'The total resistance in the circuit is: {total} ohms.')