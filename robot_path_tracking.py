def move(pos, dx, dy):
    return (pos[0] + dx, pos[1] + dy)
position = (0.0, 0.0)
position = move(position, 1.0, 1.0)
print(position)  # Output: (1.0, 1.0)
position = move(position, 3.0, 4.0)
print(position)  # Output: (4.0, 5.0)
x , y = position
print(round((x**2 + y**2) ** 0.5, 1))  # Output: 6.4