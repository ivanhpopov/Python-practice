favorite_places = {
    'John': ['P1', 'P2', 'P3'],
    'Kate': ['P4', 'P5', 'P3'],
    'Kim': ['P4', 'P2', 'P3'],
}

for name, places in favorite_places.items():
    print(f"{name}'s Favorite places are:")
    for place in places:
        print(place.title())
    print('--------------')