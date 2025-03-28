from prefect import task
import requests

@task(name="consult_information", log_prints=True)
def consult_information(): 
    print("Consulting information...")
    print("-" * 50)
    
    url = "https://pokeapi.co/api/v2/pokemon?limit=15&offset=0"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        names = [pokemon["name"] for pokemon in data["results"]]
        print(f"Fetched names: {names}")
        generation_rel(names)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        generation_rel([])

@task(name="generation_rel", log_prints=True)
def generation_rel(value):
    if value:
        print("Saving Pokémon names to a file...")
        file_path = "C:\\Users\\eduar\\Downloads\\pokemons.txt"
        
        # Escrevendo no arquivo TXT
        with open(file_path, 'w', encoding='utf-8') as file:
            for name in value:
                file.write(f"{name}\n")
        
        print(f"File saved successfully at {file_path}")
    else:
        print("No Pokémon names to save.")