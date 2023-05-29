from matplotlib import pyplot as plt
from matplotlib import image as img
from pandas import *

countries = ('Australia','Japan','Spain', 'Malaysia', 'Mauritius', 'Sri Lanka')

class myWeather:
    def seasons(self):
        print('Available Countries :')
        for ctry in countries:
            print(ctry)
        country = input('Enter the country: ')
        month = input('Enter the month of the year:')
        if country in countries:
            if country == 'Spain' or country == 'Japan':
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
            elif country == 'Mauritius':
                summer ={"November","December","January", "February","March", "April"}
                autum ={"May"}
                winter = {"June", "July", "August", "September"}
                spring = {"October"}
                data =read_csv('Code/weather.csv')
                months = data['Months'].to_list()
                if month in months:
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
                    else:
                        print('Invalid Month')
            elif country == 'Malaysia' or country== 'Sri Lanka':
                NortheastMonsoon = {"December","January", "February"}
                intermonsoon = {"March", "April", "October", "November" }
                southeastmoonsoon = {"May", "July", "June", "August", "September"}
                data =read_csv('Code/weather.csv')
                months = data['Months'].to_list()
                if month in months:
                    if month in NortheastMonsoon:
                        print("The season is: Northeast Monsoon")
                        moonsoonimg = img.imread('ISEimages/monsoon.png')
                        plt.imshow(moonsoonimg)
                        plt.show()
                    elif month in intermonsoon:
                        print("The season is: Inter-Monsoon")
                        intermoonsoonimg = img.imread('ISEimages/inter-monsoom.png')
                        plt.imshow(intermoonsoonimg)
                        plt.show()
                    elif month in southeastmoonsoon:
                        print ("The season is: South-East Monsoon")
                        moonsoonimg = img.imread('ISEimages/monsoon.png')
                        plt.imshow(moonsoonimg)
                        plt.show()
                else:
                    print('Invalid Month')
            elif country == 'Australia':
                data =read_csv('Code/weather.csv')
                months = data['Months'].to_list()
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

    def temperature(self):

        cities = {
            'Perth': {'morning_temp': 18.2, 'afternoon_temp' :23.0 }, 
            'Adelaide' : {'morning_temp': 16.5, 'afternoon_temp' :21.0 }, 
            }
        print("Available cities:")
        for city in cities:
            print(city)
        # Prompt the user to enter a city
        user_city = input("Enter the name of a city from the above options: ")
        # Check if the entered city is valid
        if user_city in cities:
            print("Valid city entered:", user_city)
            city_temp = cities [user_city]
            morning = city_temp['morning_temp']
            afternoon = city_temp['afternoon_temp']
            #using 24hr clock
            time =int(input("what time is it? "))
            temp = round(float(input ("What is the temperature today? ")), 1)
            print(temp)
            if (time > 12):
                if(temp > afternoon):
                    print("The temperature is above average")
                elif(temp < afternoon):
                    print("The temperature is below average")
                else:
                    print("The temperature is the average temperature at this time of day")
                temp_diff = temp - afternoon
                if (temp_diff > 5):
                    print("The temperature differs from the average temperature by 5 or more")  
                    print("The average temperature at this time of day is:", afternoon)

                else:
                    print("The average temperature at this time of day is:", afternoon)
            else:
                if(temp > morning):
                    print("The temperature is above average")
                else:
                    print("The temperature is below average")
                temp_diff = temp - morning
                if (temp_diff > 5):
                    print("The temperature differs from the average temperature by 5 or more") 
                    print("The average temperature at this time of day is:", morning) 
                else:
                    print("The average temperature at this time of day is:", morning)
        else:
            print("Invalid city entered.")

weather = myWeather()
weather.seasons()
weather.temperature()
