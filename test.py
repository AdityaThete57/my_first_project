import math




import numpy as np
t = np.linspace(0, 10, 5)
print(t)

x = "5"
y = 3
print(x + str(y))

for i in range(2, 10, 3):
    print("Tick")

line = "EngineA ; 1500 ; 82.5 "
parts = line.split(';')
rpm = int(parts[1].strip())
print(rpm)
#Where should the try / except block be placed to process a file that may contain occasional bad rows? The try/except block should be placed around the code that processes each row of the file. This way, if a bad row is encountered, the exception can be caught and handled without stopping the entire processing of the file. Here's an example of how you might structure it:

with open('data.txt', 'r') as file:
    for line in file:
        try:
            # Process the line (e.g., parse values, perform calculations)
            parts = line.split(';')
            rpm = int(parts[1].strip())
            print(rpm)
        except ValueError as e:
            print(f"Error processing line: {line.strip()} - {e}")
        except IndexError as e:
            print(f"Error processing line: {line.strip()} - {e}")
#list index out of range error occurs when you try to access an index that does not exist in a list. For example, if you have a list with 3 elements and you try to access the 4th element (index 3), you will get this error. To avoid this, always check the length of the list before accessing an index.
