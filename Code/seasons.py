from matplotlib import pyplot as plt
from matplotlib import image as img
from pandas import *

countries = ('Australia','Japan','Spain', 'Malaysia', 'Mauritius', 'SriLanka')

class myWeather:
    def seasons(self):
        print('Available Countries :')
        for ctry in countries:
            print(ctry)
        country = input('Enter the country: ')
        if country in countries:
            if country == 'Spain':
                data =read_csv('Code/weather.csv')
                months = data['Months'].to_list()
                seasons = data['Seasons'].tolist()
                month = input('Enter the month of the year:')
                if month in months:
                    index = months.index(month)
                    season = seasons[index]   
                    print(f'The season is: {season}')
                    if season == 'Summer':
                        summerimg = img.imread('ISEimages/summer.png')
                        plt.imshow(summerimg)
                        plt.show()     
                else:
                    print('Invalid Month')
        else:
            print('Enter a valid country')
                


weather = myWeather()
weather.seasons()
