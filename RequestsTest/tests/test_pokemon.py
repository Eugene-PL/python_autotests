import requests
import pytest

URL='https://api.pokemonbattle.ru'
TOKEN='902a46fe46d1526df0277bc42a51ee00'
TRAINER_NAME='Johny Flyer'
HEADER={'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID=33861

def test_status_code():
    response_1=requests.get(url=f'{URL}/v2/trainers',params={'trainer_id':TRAINER_ID})
    assert response_1.status_code==200

def test_trainer_name():
    response_2=requests.get(url=f'{URL}/v2/trainers',params={'trainer_id':TRAINER_ID})
    assert response_2.json()["data"][0]["trainer_name"]==TRAINER_NAME
