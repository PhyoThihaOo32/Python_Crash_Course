from cars import Car
from ev_battery import EVBattery

class ElectricCar(Car):
    number_of_electric_car_made = 0

    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery_type = EVBattery()
        ElectricCar.number_of_electric_car_made += 1
    
    def describe_battery(self):
        print(f"Battery type: {self.battery_type}")

    def check_number_of_electric_car_made(self):
        print(f'Total electric cars made: {ElectricCar.number_of_electric_car_made}')

    def charging(self):
        print("This car needs to be charged with electricity.")

    

