import random
average_temp = 0
index = 0
temp_list = []
for i in range(20):
    temp = random.randint(-10,40)
    temp_list.append(temp)
    average_temp = sum(temp_list) / len(temp_list)
print(f'The list of temperature readings is: {temp_list}')
print(f'The average temperature is: {average_temp} degree celsius.')
#If temp in temp_list < 0: doesn't work as it searches if this particular value is in the list
#For comparing each element in list to 0, we need to use for loop
for temp in temp_list:
    if temp < 0:
        index += 1
print(f'There are {index} readings below freezing.')
