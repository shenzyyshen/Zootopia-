import json
import os

print("📁 Current working directory:", os.getcwd())
print("📄 Files in this directory:", os.listdir())

"""file path"""
json_file = "animals_data.json"
html_template_file = "animals_template.html"
output_file = "animals_output.html"

"""Load an return json file"""
def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

"""Build the html string for all animals"""
def serialize_animal(animal):
    name = animal.get("name", "unknown")
    diet = animal.get("diet", "unknown")
    locations = animal.get("locations", [])
    first_location = locations[0] if locations else "Unknown"
    animal_type = animal.get("type", "Unknown")

    print(f"name:", {name})
    print(f"Diet:", {diet})
    print(f"location:", {first_location})
    print(f"Type:", {animal_type})
    print()

    """Card HTML"""
    return (
    '<li class="cards__item">\n'
    '<div class="card">\n'
    f"<h3>{name}</h3>\n"
    f"<p><strong>Diet:</strong> {diet}</p>\n"
    f"<p><strong>First location:</strong> {first_location} </p>\n"
    f"<p><strong>Type:</strong> {animal_type}</p>\n"
    '</div>\n'
    '</li>\n'
    )

"""path to data file"""
if os.path.exists(json_file) and os.path.exists(html_template_file):
    data = load_data(json_file)

    """ html list from individual animal str"""
    """extract skin type """
    output = ''
    all_skin_types = set()
    for animal in data:
        skin = animal.get("skin_type", "unknown")
        all_skin_types.add(skin)

    all_skin_types = sorted(all_skin_types)

    """display options """
    print("Available skin types:")
    for i, skin in enumerate(all_skin_types,1):
        print(f"{i}.{skin}")

    """user to choose"""
    selected_skin = None
    while selected_skin not in all_skin_types:
        selected_skin = input("Enter one of the above skin types: ").strip()
        if selected_skin not in all_skin_types:
            print("invalid choice. please choose exactly as displayed.")

    filtered_animals = [animal for animal in data if animal.get("skin_type", "unknown") == selected_skin]

    if not filtered_animals:
        print(f"No animals found with skin_type '{selected_skin}'")
        exit()
    output = ''
    for animal in filtered_animals:
        output += serialize_animal(animal)

    """Read html template"""
    with open(html_template_file, "r") as template_file:
            html_template = template_file.read()

    """Replace placeholder with animal html"""
    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    """final html output"""
    with open(output_file, "w") as file:
        file.write(final_html)

    print(f"HTML file generated successfully as '{output_file}'")
else:
    print(f"Required files not found")
    exit()

print(f"loaded {len(data)} animals")

