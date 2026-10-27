count = 0
while count < 5:#condition and an iteration
    print(count)
    count += 1#something in the loop that changes the condition

x = float(input("Enter a number: "))
print("The square of", x, "is", x**2)

guess = x/2
tolerance = 1e-6
while abs(guess**2 - x) > tolerance:
    guess = (guess + x/guess) / 2
print("The square root of", x, "is approximately", guess)
#explain what the code does
#The code consists of three main parts:
#1. The first part is a while loop that counts from 0 to 4. It initializes a variable `count` to 0 and continues to loop as long as `count` is less than 5. Inside the loop, it prints the current value of `count` and then increments `count` by 1.
#2. The second part prompts the user to enter a number and then calculates and prints the square of that number.
#3. The third part uses Newton's method to approximate the square root of the entered number. It initializes a guess to half the input value and continues to improve the guess until the difference between the square of the guess and the input value is less than a specified tolerance.
flow = 12.3456789
print(f"The flow value is approximately {flow:.3f}")
#A beam is considered safe if its deflection is between 0.5 mm and 2.0 mm inclusive. write code to check if a given deflection value is safe or not.
deflection = float(input("Enter the deflection value in mm: "))
for i in range(1,10,3):
    print('tick')
total = 0
i = 1
while i <= 4:
    total += i
    i += 1
print(total)
result = [x * 2 for x in range(5) if x % 2 == 1]
print(result)
line = 'engine1; 1200 '
parts = line.split(';')
rpm = int(parts[1].strip())
print(rpm)
materials = {
    "Steel":     7850,
    "Aluminium": 2700,
    "Copper":    8960
}

for name, density in materials.items():
    print(f"{name}: {density}")
readings = [22, 18, 35, 27, 35, 19]
readings = [22, 18, 35, 27, 35, 19]