import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

print(API_KEY)

def fetch_data(animal_name):

    """fetched the animals data for the animal 'animal_name'.
    returns: a list of animals, each animal is a dictonary """

    url = f"https://api.api-ninjas.com/v1/animals"
    headers = {
        "X-Api-key": "wnskUoJVOwCSgMvLY3QsBg==DIfm2EJM1oWQFYTL"
    }
    params = {
        "name": animal_name
    }
    response = requests.get(url, headers=headers, params=params)

    print(f"Fetching data for: {animal_name}")
    print(f"Full URL: {response.url}")

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        print(response.text)
        return []

