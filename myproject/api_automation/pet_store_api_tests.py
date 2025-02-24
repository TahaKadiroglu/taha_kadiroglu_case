import unittest
import requests


class TestPetAPI(unittest.TestCase):

    def test1_create_pet(self):

        url = "https://petstore.swagger.io/v2/pet"
        payload = {
            "id": 1661,
            "category": {
                "id": 1661,
                "name": "cats"
            },
            "name": "boncuk",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
            }
        response = requests.post(url, json=payload)
        
        # Positive scenario
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "boncuk")
        self.assertEqual(response.json()["category"]["name"], "cats")
        self.assertEqual(response.json()["status"], "available")

        # Negative scenario
        self.assertNotEqual(response.json()["status"], "notavailable")
        invalid_payload = {"id": "not integer"}  
        response = requests.post(url, json=invalid_payload)
        self.assertEqual(response.status_code, 500)

    
    def test2_get_pet(self):
        
        url = "https://petstore.swagger.io/v2/pet/1661"

        # Positive scenario
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Negative scenario
        url = "https://petstore.swagger.io/v2/pet/3333333"
        response = requests.get(url)
        self.assertEqual(response.status_code, 404)


    def test3_update_pet(self):

        url = "https://petstore.swagger.io/v2/pet"
        payload = {
            "id": 1661,
            "name": "komur",
            "status": "not available"
            }
        response = requests.put(url, json=payload)

        # Positive scenario
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "komur")

        # Negative scenario
        payload = {
            "id": 1661,
            "name": [1,2,3],
            }
        response = requests.put(url, json=payload)
        self.assertEqual(response.status_code, 500)

    
    def test4_delete_pet(self):

        url = "https://petstore.swagger.io/v2/pet/1661"

        # Positive scenario
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)

        # Negative scenario
        url = "https://petstore.swagger.io/v2/pet/3333333"
        response = requests.delete(url)
        self.assertEqual(response.status_code, 404)