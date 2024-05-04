import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\Assets\IT Courses\Cybersecurity\Pandas-Practice\data\covid-data.csv')
dataDF = pd.DataFrame(data)

# Shows new cases over days after 12/31/19 & highest number of cases in that time period
def newCases():
    days = int(input("How many days after December 31, 2019 would you lke to look at? "))
    filtered_data = data.head(days + 1)
    x = filtered_data["date"]
    y = filtered_data["new_cases"]

    plt.plot(x, y)
    plt.xlabel("Days since December 31, 2019")
    plt.ylabel("Number of New Cases")
    plt.title("New Cases")
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    max_cases = filtered_data['new_cases'].max()
    date = filtered_data.loc[filtered_data["new_cases"] == max_cases, "date"].iloc[0]
    print(f"The highest number of cases, {max_cases}, were seen on {date} within the given timeframe")
    plt.show()

# shows the number of deaths compared by country and which country highest number of deaths
def deathsOverTime():
    letter = input("Please enter the first letter of the country you would like to see: ").upper()

    country_data = data[data['location'].str.startswith(letter)]
    x = country_data['total_deaths']
    y = country_data['location']
    plt.xlabel("Country Name")
    plt.ylabel("Number of Total Deaths")
    plt.title("Total Deaths Grouped by Country")
    plt.bar(y, x, color='red')
    plt.xticks(rotation=45)
    plt.tight_layout() #easier read

    max_num = country_data['total_deaths'].max()
    country = country_data.loc[country_data["total_deaths"] == max_num, "location"].iloc[0]
    print(f"{country} had the highest number of deaths with {max_num:.0f} dead")
    plt.show()

#stats about specifc country: deaths, population, life expantency,
# aged 65 older, median age, handwashing_facilities,gdp_per_capita, etc.
def specificCountry():
    #numbers and names of countries
    array = sorted(set(dataDF['location']))
    countries = ", ".join(array)
    loc = input(f"Pick a country from the list: \n{countries}\n")

    query = input("Which of the following would you like to know? Type in the corresponding number: \n1. Total Number of Deaths \n2. Population \n3. Life Expantency \n4. Citizens Aged 65+ \n5. Median Age \n6. Number of Hygine Facilities \n7. GDP per Capita \n8. Name of Continent ")

    # no work properly
    if loc in array:
        filter = data[data['location'] == loc]
    else:
        print("Country Not Found in List")

    result = None

    if '1' in query:
        result = filter['total_deaths'].iloc[-1]
        print(f"The total deaths caused by COVID-19 in {loc} are:{result: .0f}")
    elif '2' in query:
        result = filter['population'].iloc[-1]
        print(f"The population in {loc} is:{result: .0f}")
    elif '3' in query:
        result = filter['life_expectancy'].iloc[-1]
        print(f"The life expectancy in {loc} is {result:.0f} years")
    elif '4' in query:
        result = filter['aged_65_older'].iloc[-1]
        print(f"Number of people aged 65+ in {loc}: {result*1000:.0f}")
    elif '5' in query:
        result = filter['median_age'].iloc[-1]
        print(f"The median age of people infected with COVID-19 in {loc} is: {result}")
    elif '6' in query:
        result = filter['handwashing_facilities'].iloc[-1]
        print(f"The number of hygene facilities in {loc} is: {result}")
    elif '7' in query:
        result = filter['gdp_per_capita'].iloc[-1]
        print(f"The GDP per capital in {loc} is: {result}")
    elif '8' in query:
        result = filter['continent'].iloc[0]
        print(f"{loc} is located in: {result}")
    else:
        print("Invalid Response")

type = str(input("Which of the following would you like to learn about? Type in the corresponding number: \n1. New COVID-19 Cases Since Dec 31st, 2019 \n2. Total Deaths caused by COVID-19 sorted by Country \n3. Details About a Specific Country\n"))
if '1' in type:
    newCases()
elif '2' in type:
    deathsOverTime()
elif '3' in type:
    specificCountry()
else:
    print("Invalid choice, please pick a number 1 to 3.")