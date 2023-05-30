import unittest

from seasons import myWeather
from pandas import *
class MyWeatherTests(unittest.TestCase):
    def test_invalid_country(self):
        expected_output = 'Invalid country'
        weather = myWeather()
        actual = weather.seasons('Germany', 'June')
        self.assertEqual(expected_output, actual, "Invalid country")

    def test_invalid_month(self):
        expected_output = 'Invalid Month'
        weather = myWeather()
        actual = weather.seasons('Japan', 'Jack')
        self.assertEqual(expected_output, actual)

    def test_valid_country(self):
        expected_output = 'The season is: Summer'
        weather = myWeather()
        actual = weather.seasons("Spain", "July")
        self.assertEqual(expected_output, actual)
    
    # def test_temperature(self):
    #     expected_output = "The temperature is above average"
    #     weather = myWeather()
    #     temp = 20.0
    #     actual = weather.temperature(temp)
    #     self.assertEqual(expected_output, actual)
    def testseasonsFile(self):
            try:
                data = read_csv('weather.csv')
                # Assert that the data variable is not None
                self.assertIsNotNone(data)
            except FileNotFoundError:
                self.fail("file not found")
    def testSeasonFile(self):
        myWeather.seasons("weather.csv", "Months", "Seasons" )
        with open("weather.csv") as outFile:
            self.assertEqual("Months,Seasons\n", outFile.readline())
if __name__ == '__main__':
    unittest.main()
