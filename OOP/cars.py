class Car:

    number_of_car_made = 0

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        Car.number_of_car_made += 1

    def describe_car(self):
        print(
            f"Manufacturer: {self.manufacturer}\n"
            f"Model: {self.model}\n"
            f"Year: {self.year}"
        )
        

    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it")

    def set_odometer(self, mileage):
        if mileage >= 0:
            self.odometer_reading = mileage
        else:
            print("Odometer reading cannot be negative.")

    def update_odometer(self, new_mileage):
        if new_mileage >= self.odometer_reading:
            self.odometer_reading = new_mileage
        else:
            print("Don't you even try to roll back the odometer!")

    def increase_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Don't you even try to roll back the odometer!")

    def charging(self):
        print("This car uses gasoline.")

class EVBattery:
    def __init__(self, battery_type='Standard Li-ion 60Ah', capacity_kwh=60, voltage=400):
        self.battery_type = battery_type
        self.capacity_kwh = capacity_kwh
        self.voltage = voltage

    def describe_battery(self):
        print(f"Battery Type: {self.battery_type}")
        print(f"Capacity (Default): {self.capacity_kwh} kWh")
        print(f"Voltage: {self.voltage} V")

    def upgrade_battery(self, capacity_kwh=None):
        if capacity_kwh is None:
            try: 
                capacity_kwh = int(input('Set new capacity_kwh: '))
            except ValueError:
                print('Invalid input. Upgrade cancelled.')
                return
        self.capacity_kwh = capacity_kwh
        print(f'Upgraded battery capacity: {self.capacity_kwh}')

    def estimate_range(self):
        # Basic mock estimation: 5 km per kWh
        self.estimated_range = self.capacity_kwh * 5
        print(f"Estimated Range: {self.estimated_range} km")

class ElectricCar(Car):
    number_of_electric_car_made = 0

    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery_type = EVBattery('22kwh Lion 60ah')
        ElectricCar.number_of_electric_car_made += 1
    
    def describe_battery(self):
        print(f"Battery type: {self.battery_type}")

    def check_number_of_electric_car_made(self):
        print(f'Total electric cars made: {ElectricCar.number_of_electric_car_made}')

    def charging(self):
        print("This car needs to be charged with electricity.")

    
my_tesla = ElectricCar('Tesla', 'Tesla_Model_Y',2022)

my_tesla.describe_car()
my_tesla.describe_battery()
my_tesla.check_number_of_electric_car_made()
my_tesla.battery_type.describe_battery()
my_tesla.battery_type.estimate_range()
my_tesla.battery_type.upgrade_battery()
my_tesla.battery_type.estimate_range()

# call only the parent version of charging()
# super(ElectricCar, my_tesla).charging()
# or
# Car.charging(my_tesla)
