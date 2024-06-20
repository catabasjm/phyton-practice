capitals = {'usa': 'washington dc',
            'india': 'new delhi',
            'china': 'beijing',
            'russia': 'moscow'}
print(capitals['russia'])

print(capitals.get('germany'))  # to check if an elements exists
print(capitals.keys())
print(capitals.values())  # value inside key
print(capitals.items())   # all items

capitals.update({'germany': 'berlin'})  # to add new element or edit value
capitals.pop('china')  # removes value and key

for key,value in capitals.items():
    print(key, value)

# dictionary comprehension
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}


cities_in_F = {'new york': 32, 'boston': 75, 'los angles': 100, 'chicago': 50}

cities_in_C = {key: round((value-32) * (5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

weather = {'new york': 'sunny', 'boston': 'rainy', 'los angles': 'sunny', 'chicago': 'cloudy'}
sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(sunny_weather)

# cities = {'new york': 32, 'boston': 75, 'los angles': 100, 'chicago': 50}
# desc_cities = {key: ('warm' if value >= 40 else 'cold') for (key, value) in cities.items()}
# print(desc_cities)


def check_temp(value):
    if value >=70:
        return "hot"
    elif 69 >= value >= 40:
        return 'warm'
    else:
        return 'cold'

cities = {'new york': 32, 'boston': 75, 'los angles': 100, 'chicago': 50}
desc_cities = {key: (check_temp(value)) for (key, value) in cities.items()}
print(desc_cities)