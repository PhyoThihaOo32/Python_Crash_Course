def make_cars(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key, value in car_info.items():
        print(f'{key}: {value}')
    return car_info

first_car = make_cars(model='RAV4', manufacturer='Toyota', year= 2025, drive_type = 'AWD', exterior_color = 'Black')

