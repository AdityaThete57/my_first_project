density_of = {
    "Aluminium" : 2700,
    "Steel" : 7850,
    "Copper" : 8960,
}
print(density_of["Aluminium"])

materials = {
    "Aluminium" :{"density": 2700, "youngs": 69e9},
    "Steel" : {"density": 7850, "youngs": 200e9},
    "Copper" : {"density": 8960, "youngs": 120e9},
}
#title() converts the first letter of each word to uppercase and the rest to lowercase
#while None is returned if the key is not found in the dictionary, and you can keep asking user for input

print(materials["Aluminium"])
#materials["Titanium"] #KeyError: 'Titanium'
materials.get("Titanium") #None
print(materials.get("Steel"))
          