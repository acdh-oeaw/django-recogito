import json
from django.test import TestCase
from recogito.models import RecogitoAnnotation


class RecogitoAnnotationTestCase(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        # Test definitions as before.
        pass

    def test_001_model_count(self):
        # A test that uses the fixtures.
        items = RecogitoAnnotation.objects.all()
        self.assertEqual(items.count(), 3)

    def test_002_details(self):
        response = self.client.get('/api/recogitoannotations/')
        self.assertEqual(response.status_code, 200)

    def test_003_details(self):
        response = self.client.get('/api/recogitoannotations/?format=recogito')
        self.assertEqual(response.status_code, 200)

    def test_004_details(self):
        response = self.client.get('/api/recogitoannotations/?format=recogito')
        data = json.loads(response.content)[0]
        self.assertTrue('@context' in data.keys())
