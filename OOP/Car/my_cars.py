from cars import Car
from ev_battery import EVBattery
from electric_car import ElectricCar

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

my_toyota = Car('Toyota', 'Corolla', 2023)
my_toyota.describe_car()