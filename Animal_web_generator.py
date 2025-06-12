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
#file path
json_file = "animals_data.json"
html_template_file = "template.html"
output_file = "animals_template.html"

with open("animals_data.json") as f:
    data = json.load(f)


"""path to data file"""
if os.path.exists(json_file) and os.path.exists(html_template_file):
    animals_data = load_data(json_file)


    # build the html content string for all animals
    animal_cards = ""

    for animal in animals_data:


        name = animal.get("name", "unknown")
        diet = animal.get("diet" "unknown")
        locations = animal.get("locations", [])
        first_location = locations[0] if locations else "Unknown"
        animal_type = animal.get("type", "Unknown")

        print("name:", name)
        print("Diet:", diet)
        print("location:", first_location)
        print("Type:", animal_type)
        print()


        #html blocks
        card = f"""
                <li class="cards__item">
                    <div class="card">
                        <h3>{name}</h3>
                        <p><strong>Diet:</strong> {diet}</p>
                        <p><strong>First Location:</strong> {first_location}</p>
                        <p><strong>Type:</strong> {animal_type}</p>
                    </div>
                </li>
                """
        animal_cards += card


    with open(html_template_file, "r") as template_file:
        html_template = template_file.read()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO_", animal_cards)

    with open(output_file, "w") as file:
        file.write(final_html)

    print(f"HTML file generated successfully as '{output_file}'")

else:
    print(f"Required files not found")
    exit()


