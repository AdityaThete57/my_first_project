internal_pressure = float(input('Enter the internal pressure of the pressure vessel being tested (in bars): '))
wall_temp = float(input('Enter the temperature of the pressure vessel being tested (in degree celsius): '))
vibration_level = float(input('Enter the vibration level of the pressure vessel being tested (in mm): '))
internal_pressure_ok = 5<=internal_pressure<=15
wall_temp_ok = 20<=wall_temp<=250
vibration_level_ok = vibration_level < 4
if internal_pressure_ok and wall_temp_ok and vibration_level_ok:
    print('The pressure vessel is safe.')
else:
    print('The pressure vessel is not safe.')
    if not internal_pressure_ok:
        print('The internal pressure value does not match the requirement range.')
    if not wall_temp_ok:
        print('The wall temperature value does not match the requirement range.')
    if not vibration_level_ok:
        print('The vibration level value does not match the requirement range.')
        
