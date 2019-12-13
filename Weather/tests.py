from app import app
from unittest import TestCase, main
from unittest.mock import patch

class AppTests(TestCase): 
    """Run tests on the Weather App."""
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

@patch('app.requests')
def test_weather_results(self, requests):
    requests.get().json.return_value = {
        'main': { 'temp': 60 }
    }
    result = self.app.get('/weather_results?city=San+Francisco')
    self.assertEqual(result.status_code, 200)

    page_content = result.get_data(as_text=True)
    self.assertIn('It is now 60 degrees Fahrenheit', page_content)


if __name__ == '__main__':
    main()