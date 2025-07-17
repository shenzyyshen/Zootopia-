# 🦁 Zootopia Animal Info Generator

**Zootopia** is a Python-based web content generator that allows users to:
- Search for animals by name (via the [API Ninjas Animals API](https://api-ninjas.com/api/animals)),
- Filter them based on their skin type (e.g. fur, scales, skin),
- Generate a clean HTML page with detailed animal information.

---

## 🚀 Features

- Live data fetching from a public API
- Flexible data filtering by skin type
- Generates dynamic, styled HTML content
- Modular architecture: separate data fetching and UI logic
- Protects sensitive API keys using `.env`

---

## 📁 Project Structure

Zootopia/
-.env #API KEY
-.gitignore #prevents commiting sensitive files
-README.md #project overview and setup instructions 
-requirements.txt #python dependencies 

-animal_web_generator.py #Main logic: prompts + html generation
-data_fetcher.py #Seperate module to fetch data from API
-animals_template.html #HTML layout with placeholder for animal content
-animals_output.html #final generated HTML output
-animals_data.json #optional but local static data
-data_fetcher.py #fetches animal data from the API

---

## 📦 Requirements

You need:

- Python 3.7 or newer
- A free [API Ninjas](https://api-ninjas.com/api/animals) account (for your API key)

---

## 💻 Installation

To install this project:

1. Clone the repository:

```bash
git clone https://github.com/your-username/Zootopia.git
cd Zootopia

pip install -r requirements.txt

---

## Contributions are always welcomes, feel free to fork this repo,and open a pull request.
Thanks for cheking it out. 
