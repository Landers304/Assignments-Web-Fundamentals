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

def fetch_planet_data():
    # API endpoint for fetching planet data
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
    # Make a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        planets = response.json()['bodies']  # Parse JSON response

        # Process each planet's info
        for planet in planets:
            if planet['isPlanet']:  # Check if it's a planet
                name = planet['englishName']  # Get planet English name
                mass = planet['mass']['massValue']  # Get planet mass
                orbit_period = planet['sideralOrbit']  # Get planet orbit period

                # Print the planet information
                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    else:
        print("Error fetching planet data:", response.status_code)

# Fetch and display planet data
fetch_planet_data()

# Run the Spript:

# python fetch_planet_data.py




# Task 3: 


import requests

def fetch_planet_data():
    # API endpoint for fetching planet data
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    
    # Make a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        planets = response.json()['bodies']  # Parse JSON response
        formatted_planets = []

        # Process each planet's info
        for planet in planets:
            if planet['isPlanet']:  # Check if it's a planet
                name = planet['englishName']  # Get planet English name
                mass = planet['mass']['massValue']  # Get planet mass
                orbit_period = planet['sideralOrbit']  # Get planet orbit period

                # Append formatted planet data to the list
                formatted_planets.append({
                    'name': name,
                    'mass': mass,
                    'orbit_period': orbit_period
                })

        return formatted_planets
    else:
        print("Error fetching planet data:", response.status_code)
        return []

def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0

    for planet in planets:
        if planet['mass'] > max_mass:  # Check if current planet is heavier
            max_mass = planet['mass']
            heaviest_planet = planet

    return heaviest_planet['name'], heaviest_planet['mass']

def find_longest_orbit_period(planets):
    longest_orbit_planet = None
    max_orbit_period = 0

    for planet in planets:
        if planet['orbit_period'] > max_orbit_period:  # Check for longest orbit period
            max_orbit_period = planet['orbit_period']
            longest_orbit_planet = planet

    return longest_orbit_planet['name'], longest_orbit_planet['orbit_period']

# Main execution
planets = fetch_planet_data()

# If planets data was fetched successfully
if planets:
    name, mass = find_heaviest_planet(planets)
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")

    longest_name, longest_orbit = find_longest_orbit_period(planets)
    print(f"The planet with the longest orbit period is {longest_name} with an orbit period of {longest_orbit} days.")



# Run the Script:

# python fetch_planet_data.py
