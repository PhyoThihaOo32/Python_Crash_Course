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

