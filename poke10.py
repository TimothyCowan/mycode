from pprint import pprint

import requests


def main():
    poke_request = 'https://pokeapi.co/api/v2/pokemon-habitat/'
    pokejson = (requests.get(poke_request)).json()
    count = 0

    for area in pokejson['results']:  #prints each habitat
        print('############' + area['name'])
        count = count + 1
        poke_request = poke_request + str(count)  #change orginal api url by cat'ing url with count++
        pokejson_append = (requests.get(poke_request)).json()

        for pokemon in pokejson_append['pokemon_species']:  #todo Fix: Bug at start of this for loop
            print(pokemon['name'])


if __name__ == "__main__":
    main()
