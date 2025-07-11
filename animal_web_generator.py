import json
import os
import data_fetcher

"""
print("📁 Current working directory:", os.getcwd())
print("📄 Files in this directory:", os.listdir())
"""

"""file path"""
json_file = "animals_data.json"
html_template_file = "animals_template.html"
output_file = "animals_output.html"


"""Build the html string for all animals"""
def serialize_animal(animal):
    name = animal.get("name", "unknown")
    diet = animal.get("diet", "unknown")
    locations = animal.get("locations", [])
    first_location = locations[0] if locations else "Unknown"
    animal_type = animal.get("type", "Unknown")


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
if os.path.exists(html_template_file):

    animal_name = ""
    while not animal_name:
        animal_name = input("Please enter an animal to search: ").strip().lower()
        if not animal_name:
            print("Please enter a valid animal name, ")

    data = data_fetcher.fetch_data(animal_name)

    if not data:
        message = (
        f'<h2 style="color: orange; text-align: center;">'
        f'The animal"{animal_name}" does not exist in our world.'
        f'</h2>'
        )
        with open(html_template_file, "r") as template_file:
            html_template = template_file.read()

        final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", message)

        with open(output_file, "w") as file:
            file.write(final_html)

        print(f"No data found.html message generated in '{output_file}'")
        exit()

    """ html list from individual animal str"""
    """extract skin type """
    output = ''

    all_skin_types = set()
    for animal in data:
        skin_type = (animal.get("characteristics", {}).get("skin_type") or "Unknown").capitalize()
        skin_type = skin_type.strip().title()
        all_skin_types.add(skin_type)

    all_skin_types = sorted(all_skin_types)

    """display options """
    print("Available skin types:")
    for i, skin in enumerate(all_skin_types, 1):
        print(f"{i}.{skin}")

    """user to choose"""
    selected_skin = None
    while selected_skin not in all_skin_types:
        user_input = input("Enter one of the above skin types: ").strip().capitalize()
        if user_input in all_skin_types:
            selected_skin = user_input
        else:
            print("Invalid choice. please choose exactly as displayed.")

    """filtering logic"""
    filtered_animals = [
        animal for animal in data
        if (animal.get("characteristics", {}).get("skin_type") or "Unknown").capitalize() == selected_skin
    ]
    print(f"found {len(filtered_animals)} animal(s) with skin_type '{selected_skin}'")

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

