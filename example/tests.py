from django.test import TestCase
from example.models import MyText


class ExampleTestCase(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        # Test definitions as before.
        pass

    def test_001_model_count(self):
        items = MyText.objects.all()
        self.assertEqual(items.count(), 1)

    def test_002_details(self):
        response = self.client.get('/my-text/1/')
        self.assertEqual(response.status_code, 200)

    def test_003_str_method(self):
        item = MyText.objects.first()
        self.assertTrue(item.__str__(), "Homer: The Odyssey")
