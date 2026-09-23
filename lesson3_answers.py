#Exercise 1
import math
mast_shadow_length = float(input('Enter the length of the shadow of radio mast from the mast to the tip of the shadow in metres: '))
angle_of_elevation = float(input('Enter the angle of elevation in radians: '))
mast_distance_from_surveyor = mast_shadow_length / math.cos(angle_of_elevation)
mast_height = mast_distance_from_surveyor * math.sin(angle_of_elevation)
print(f"The height of the mast is {mast_height:.3f} metres.")
print(f"The distance between the surveyor to the top of the mast is {mast_distance_from_surveyor} metres.")
#Exercise 2
user_pH = float(input('Enter a pH value: '))
if user_pH < 6.5:
    print('pH is Acidic.')
elif user_pH >= 6.5 and user_pH <= 8.5:
    print('pH is neutral/ safe.')
else:
    print('pH is Alkaline.')