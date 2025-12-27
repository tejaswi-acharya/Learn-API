import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    # print(response)    #200 means that the response from the server was okay
    if response.status_code==200:
        data_pokemon=response.json()
        # print(data_pokemon)
        # print("Successful in retrieving data!")
        return data_pokemon
        
    else:
        print(f"Failed to retrieve the data:{response.status_code}")


pokemon_name = input("Enter the name of Pokemon:")
pokemon_info=get_info_pokemon(pokemon_name)
print(f"Name:{pokemon_info['name'].capitalize()}")
print(f"Id:{pokemon_info['id']}")
print(f"Height:{pokemon_info['height']}")
print("success!!!!!")