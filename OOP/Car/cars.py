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

