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

            elif country == 'Australia':
                data =read_csv('Code/weather.csv')
                months = data['Months'].to_list()
                month = input('Enter the month of the year:')
                if month in months:
                    types= 'Meteorological', 'Noongar'
                    print("The available calendar type are:")
                    for seasontype in types:
                        print(seasontype)
                    calendar = input('Please enter the season type: ')
                    if calendar in types:
                        print('The season type chosen is', calendar)
                        if calendar =="Meteorological":
                            summer ={"January", "February" , "December"}
                            autum ={"March", "April", "May"}
                            winter = {"June", "July", "August"}
                            spring = {"September", "October", "November"}
                            if month in summer:
                                print("The season is: summer")
                                summerimg = img.imread('ISEimages/summer.png')
                                plt.imshow(summerimg)
                                plt.show()
                            elif month in autum:
                                print("The season is: autumn")
                                autumnimg = img.imread('ISEimages/autumn.png')
                                plt.imshow(autumnimg)
                                plt.show()
                            elif month in winter:
                                print ("The season is: winter")
                                winterimg = img.imread('ISEimages/winter.png')
                                plt.imshow(winterimg)
                                plt.show()
                            elif month in spring:
                                print("The season is: spring")
                                springimg = img.imread('ISEimages/spring.png')
                                plt.imshow(springimg)
                                plt.show()
                        elif calendar =="Noongar":
                            Birak ={"January","December"}
                            Bunuru ={"March", "February"}
                            Djeran ={"April", "May"}
                            Makuru = {"June", "July"}
                            Dijiba ={"August", "September"}
                            Kambarang = {"October", "November"}
                            if month in Birak:
                                print("The season is: Birak")
                                birakimg = img.imread('ISEimages/birak.png')
                                plt.imshow(birakimg)
                                plt.show()
                            elif month in Bunuru:
                                print("The season is: Bunuru")
                                bunuruimg = img.imread('ISEimages/bunuru.png')
                                plt.imshow(bunuruimg)
                                plt.show()
                            elif month in Djeran:
                                print ("The season is: Djeran")
                                djeranimg = img.imread('ISEimages/djeran.png')
                                plt.imshow(djeranimg)
                                plt.show()
                            elif month in Makuru:
                                print("The season is: Makuru")
                                makuruimg = img.imread('ISEimages/makuru.png')
                                plt.imshow(makuruimg)
                                plt.show()
                            elif month in Dijiba:
                                print("The season is: Dijiba")
                                dijibaimg = img.imread('ISEimages/makuru.png')
                                plt.imshow(dijibaimg)
                                plt.show()
                            elif month in Kambarang:
                                print("The season is: Kambarang")
                                kambarangimg = img.imread('ISEimages/makuru.png')
                                plt.imshow(kambarangimg)
                                plt.show()
                    
                    else:
                        print('Enter a valid season type')  
                else:
                    print('Enter a valid month')
        
        else:
            print('Enter a valid country')
                


weather = myWeather()
weather.seasons()
