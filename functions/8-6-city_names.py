def city_name(city, country):
    x = (f"{city} is in {country}")
    return x

while True:
    city = input("Please provide city name or enter 'q' to quit.")
    if city == 'q':
        break
    country = input("Please provide country of city, or enter 'q' to quit.")
    if country == 'q':
        break

    answer = city_name(city, country)
    print(answer)


