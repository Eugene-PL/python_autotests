import requests

URL= 'https://api.pokemonbattle.ru'
TOKEN= '902a46fe46d1526df0277bc42a51ee00'
HEADER= {'Content-Type': 'application/json', 'trainer_token': TOKEN}

# 1. Cоздание покемона
response_create= requests.post(url=f'{URL}/v2/pokemons', headers=HEADER, json=
{
    "name": "generate",
    "photo_id": -1
})
print(response_create.text)
# сохранение полученного значения id покемона
pokemon_id= response_create.json()['id']
print(pokemon_id)

# 2. Cмена имени покемона
response_rename= requests.put(url=f'{URL}/v2/pokemons', headers=HEADER, json=
{
    "pokemon_id": pokemon_id,
    "name": "Cheburashka",
    "photo_id": -1
})
print(response_rename.text)

# 3. Поймать покемона в покебол
response_pokeball= requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers=HEADER, json=
{
    "pokemon_id": pokemon_id
})
print(response_pokeball.text)

# нокаут своего покемона
'''response_create= requests.post(url=f'{URL}/v2/pokemons/knockout', headers=HEADER, json=
{
 "pokemon_id": pokemon_id
})
print(response_create.text)'''
