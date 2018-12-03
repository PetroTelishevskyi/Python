import app
import unittest
import requests


class FlaskTest(unittest.TestCase):

    def testRoot(self):
        test = requests.get('http://127.0.0.1:8000/')
        return self.assertEqual(test.status_code, 200)

    def testFail(self):
        test = requests.get('http://127.0.0.1:8000/contactes')
        return self.assertEqual(test.status_code, 404)

    def testNew(self):
        test = requests.post('http://127.0.0.1:8000/new_contacts', data= ({'auditory':'auditory 123', 'surname': 'Telsihevskyi','date':'21.04.2018','time':'13:45-15:45'}))
        return self.assertEqual(test.status_code, 200)

    def testSearch(self):
        test = requests.get('http://127.0.0.1:8000/contacts')
        return self.assertEqual(test.status_code, 200)

    def testEdit(self):
        test = requests.post('http://127.0.0.1:8000/edit_contacts/<id>', data= ({'id': '1'}))
        return self.assertEqual(test.status_code, 200)

    def testDelete(self):
       test = requests.post('http://127.0.0.1:8000/contacts/delete', data= ({'id': '1'}))
       return self.assertEqual(test.status_code, 200)
if __name__ == '__main__':
    unittest.main()
