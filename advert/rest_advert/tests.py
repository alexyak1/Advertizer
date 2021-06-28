from django.test import TestCase, Client
from rest_framework import status


class AdsTest(TestCase):
    """ Test module for GET all puppies API """
    mocData = {"subject": "test subject",
        "body": "test body",
        "price": "1500",
        "email": "asdasd@assd.asd"}
    adId = 0

    def test_get_all_ads(self):
        c = Client()
        response = c.get('/ads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_ads(self):
        c = Client()
        response = c.get('/ads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_ad(self):
        c = Client()
        response = c.post('/ads/', self.mocData)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.adId = response.data.get('id')

    def test_delete_ad(self):
        c = Client()
        response = c.delete('/ads/'+str(self.adId))
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
