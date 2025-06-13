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

"""path to data file"""
if os.path.exists(json_file) and os.path.exists(html_template_file):
    data = load_data(json_file)

    """Build the html string for all animals"""
    output = ""

    for animal in data:
        name = animal.get("name", "unknown")
        diet = animal.get("diet", "unknown")
        locations = animal.get("locations", [])
        first_location = locations[0] if locations else "Unknown"
        animal_type = animal.get("type", "Unknown")

        """Card HTML"""
        output += '<li class="cards__item">\n'
        output += '<div class="card">\n'
        output += f"<h3>{name}</h3>\n"
        output += f"<p><strong>Diet:</strong> {diet}</p>\n"
        output += f"<p><strong>First location:</strong> {first_location} </p>\n"
        output += f"<p><strong>Type:</strong> {animal_type}</p>\n"
        output += '</div>\n'
        output += '</li>\n'

        print(f"name:", {name})
        print(f"Diet:", {diet})
        print(f"location:", {first_location})
        print(f"Type:", {animal_type})
        print()

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

