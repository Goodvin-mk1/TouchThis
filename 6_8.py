# Ключ - название страны,
# значение - список городов,
# на вход поступает город,
# необходимо сказать из какой он страны

your_city = input("Enter city: ")
countries_cities = {
    'Belarus': ['Minsk', 'Brest', 'Mogilev'],
    'Russia': ['Moscow', 'Petersburg', 'Omsk'],
    'USA': ['New-york', 'Chicago', 'LA']
}
counter = 0
for country in countries_cities:
    for city in countries_cities[country]:
        if your_city in city:
            print("This city from", country)
            counter += 1
            break
if counter != 1:
    print("No such city")
