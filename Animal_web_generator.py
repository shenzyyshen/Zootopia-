""" reads the content of animals_data.json,
iterates through the animals,and for each one prints:
Name
Diet
The first location from the locations list
Type"""


import json
import os

"""Load an return json file"""
def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

file_name = "animals_data.json"


#path to data file
if os.path.exists(file_name):
    data = load_data(file_name)

    for animal in data:
        name = animal.get("name")
        diet = animal.get("diet")
        location = animal.get("locations", [])
        animal_type = animal.get("type")


        print(f"Name: {name}")
        print(f"Diet: {diet}")
        print(f"first known location: {location [0] if location else 'unknown'}")
        print(f"Type: {animal_type}")
        print("-" * 30)
else:
    print(f"File '{file_name}' does not exist.")

