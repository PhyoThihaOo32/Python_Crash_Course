class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, max_capacity=100):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.max_capacity = max_capacity

    def describe_restaurant(self):
        print(f"Name of restaurant: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, current_number_served):
        if current_number_served < 0:
            print("Negative input not accepted.")
            return
        elif current_number_served > self.max_capacity:
            print(f"We can only serve up to {self.max_capacity} people at once. Setting to max capacity.")
            self.number_served = self.max_capacity
        else:
            self.number_served = current_number_served
        print(f"We are currently serving {self.number_served} customers.")

    def increase_number_served(self, additional_customers):
        if additional_customers < 0:
            print("We don't accept negative values.")
        elif self.number_served + additional_customers > self.max_capacity:
            print(f"Cannot exceed max capacity of {self.max_capacity}. Serving up to max capacity.")
            self.number_served = self.max_capacity
        else:
            self.number_served += additional_customers
        print(f"Updated number served: {self.number_served}")


