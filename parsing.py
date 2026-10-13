line = "Engine1; 1200 RPM; 85 C"
parts = line.split(";")# if you write a space after semicolon, it will be included in the parts, so we can use strip() to remove it
print(parts)

name = parts[0].strip()
field1= parts[1].strip()
field2 = parts[2].strip()
print(field1,field2)

rpm = int(field1.split()[0]) # convert the first part of field1 to an integer
temperature = int(field2.split()[0]) # convert the first part of field2 to an integer
print("RPM:", rpm, "Temperature:", temperature)

units1 = field1.split()[1] # get the second part of field1
units2 = field2.split()[1] # get the second part of field2
print("Units1:", units1, "Units2:", units2)