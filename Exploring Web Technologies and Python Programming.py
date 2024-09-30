# Task 1:



# Step 1: Use the command prompt or terminal to run the following command to create a virtual environment:

#python -m venv myenv ---- Windows

#python3 -m venv myenv ---- macOS / Linux



# Step 2:  Activate the virtual environment using the following commands:

#myenv\Scripts\activate ---- Windows

#source myenv/bin/activate ---- macOS / Linux



# Step 3: Install the request packages using pip:

# pip install requests



# Step 4: Verify the installation 

# pip freeze




# Task 2:


import requests

# Step 1: Make a GET request to the Pokémon API for Pikachu's data
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

# Check if request was successful
if response.status_code == 200:
    # Step 2: Parse the JSON data from the response
    pokemon_data = response.json()

    # Extract Pokémon's name
    name = pokemon_data['name']
    print(f"Name: {name.capitalize()}")

    # Extract Pokemon's abilities
    abilities = pokemon_data['abilities']
    print("Abilities:")
    for ability in abilities:
        ability_name = ability['ability']['name']
        print(f"- {ability_name.capitalize()}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

 # Run the Script:

 # python "c:/CodingTemple/Python Functions/Web Fundamentals.py"



# Task 3: 


import requests

# Function to fetch Pokémon data from the API
def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        print(f"Error fetching data for {pokemon_name}")
        return None

# Function to calculate the average weight of a list of Pokémon
def calculate_average_weight(pokemon_list):
    total_weight = 0
    count = len(pokemon_list)
    
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    
    average_weight = total_weight / count if count > 0 else 0
    return average_weight

# List of Pokémon names
pokemon_names = ["pikachu", "bulbasaur", "charmander"]

# List to store fetched Pokémon data
pokemon_data_list = []

# Fetch data for each Pokémon
for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data_list.append(data)

# Display the names, abilities, and average weight
if pokemon_data_list:
    print("Pokémon Details:\n")
    for pokemon in pokemon_data_list:
        # Print Pokémon's name
        print(f"Name: {pokemon['name'].capitalize()}")
        
        # Print Pokémon's abilities
        abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        print(f"Abilities: {', '.join(abilities)}")
        
        # Print Pokémon's weight
        print(f"Weight: {pokemon['weight']}")
        print("-" * 30)
    
    # Print the average weight
    average_weight = calculate_average_weight(pokemon_data_list)
    print(f"Average Weight of the Pokémon: {average_weight}")

else:
    print("No Pokémon data available.")

# Run the Script:

# python "c:/CodingTemple/Python Functions/Web Fundamentals.py"
