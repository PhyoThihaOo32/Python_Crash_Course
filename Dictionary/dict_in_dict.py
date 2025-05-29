cities = {
    'yangon': {
        'country': 'Myanmar',
        'population': 5160000,
        'fun-fact': 'Yangon is known for the Shwedagon Pagoda, a 99-meter tall stupa covered with gold leaf and precious stones.'
    },
    'new york':{
        'country': 'USA',
        'population': 8419000,
        'fun-fact': 'New York City is home to the iconic Statue of Liberty and is known as "The City That Never Sleeps."'
    },
    'tokyo':{
        'country': 'Japan',
        'population': 13960000,
        'fun-fact': 'Tokyo is the world’s most populous metropolitan area and is famous for its cherry blossoms and cutting-edge technology.'
    }
}

for city, info_information in cities.items():
    print(f'city: {city.title()} ')
    for info, information in info_information.items():
        print(f'{info}: {information}')
    