import pytest
import sys
import os
sys.path.append(os.path.abspath("/home/sebastian/GitHub/p_208_Lotnisko/Project"))
from client import Client

def test_check_crash():
    client = Client(1)
    response = {"crash": True}
    client.check_crash(response)
    assert True == client.finish

def test_load_random_position():
    client = Client(1)
    client.load_random_position()
    assert 0 <= client.json["pos_x"] <= 10000
    assert 0 <= client.json["pos_y"] <= 10000
    assert 2000 <= client.json["pos_z"] <= 5000
    assert 250 <= client.json["velocity"] <= 300

def test_check_to_many_planes():
    client = Client(1)
    response = {"command": "to_many_planes"}
    client.check_to_many_planes(response)
    assert client.finish == True


#  python3 -m pytest testClient.py -vvv
print("test")