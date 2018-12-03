import requests

def testRoot():
    test = requests.get('http://127.0.0.1:8000/')
    test.raise_for_status()
    assert test.status_code == 200

def testNew():
    test = requests.post('http://127.0.0.1:8000/new_contacts', data= ({'auditory':'auditory 123', 'surname': 'Telsihevskyi','date':'21.04.2018','time':'13:45-15:45'}))
    test.raise_for_status()
    assert test.status_code == 200
    assert test.text

def testSearch():
    test = requests.get('http://127.0.0.1:8000/contacts')
    test.raise_for_status()
    assert test.status_code == 200

def testEdit():
    test = requests.post('http://127.0.0.1:8000/edit_contacts/<id>', data= ({'id': '1'}))
    test.raise_for_status()
    assert test.status_code == 200

def testDelete():
    test = requests.post('http://127.0.0.1:8000/contacts/delete', data= ({'id': '1'}))
    test.raise_for_status()
    assert test.status_code == 200
