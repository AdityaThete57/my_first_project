def move(pos, dx, dy):
    return (pos[0] + dx, pos[1] + dy)
position = (0.0, 0.0)
position = move(position, 1.0, 1.0)
print(position)  # Output: (1.0, 1.0)
position = move(position, 3.0, 4.0)
print(position)  # Output: (4.0, 5.0)
x , y = position
print(round((x**2 + y**2) ** 0.5, 1))  # Output: 6.4

def move_altitude(x, y, altitude):
    return (altitude[0] + x, altitude[1] + y, altitude[2])
position1 = (0.0, 0.0, 0.0)
position1 = move_altitude(position1[0], position1[1], position[2])
print(position1)  # Output: (0.0, 0.0, 5.0)