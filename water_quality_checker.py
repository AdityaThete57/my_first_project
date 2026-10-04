pH = float(input('Enter the pH of water being tested: '))
temp = float(input('Enter the temperature of water being tested: '))
DO = int(input('Enter the dissolved oxygen in the water being tested: '))
pH_ok = 6.5<=pH<=8.5
temp_ok = 10<=temp<=25
DO_ok = DO > 5
if pH_ok and temp_ok and DO_ok:
    print('Water is safe')
else:
    print('Water is not Safe')
    if not pH_ok:
        print('The pH is not in the correct requirement.')
    if not temp_ok:
        print('The temperature does not fit the suitable requirement.')
    if not DO_ok:
        print("The dissolved oxygen level doesn't match the requirements.")