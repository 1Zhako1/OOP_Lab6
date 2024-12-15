class Vehicle:
    def __init__(self, color="", year="", hp="", speed_limit="", mpg=""):
        self.color = color
        self.year = year
        self.hp = hp
        self.speed_limit = speed_limit
        self.mpg = mpg

    def create_vehicle(self):
        self.color = input("Enter Vehicle's color: ")
        self.year = input("Enter Vehicle's year of manufacturing: ")
        self.hp = input("Enter Vehicle's horsepower: ")
        self.speed_limit = input("Enter Vehicle's maximum speed: ")
        self.mpg = input("Enter Vehicle's efficiency in miles per gallon: ")

    def display(self):
        print("Vehicle's Color:", self.color)
        print("Vehicle's Year:", self.year)
        print("Vehicle's Horsepower:", self.hp)
        print("Vehicle's Speed Limit:", self.speed_limit)
        print("Vehicle's MPG:", self.mpg)


class Truck(Vehicle):
    def __init__(self, color="", year="", hp="", speed_limit="", mpg="", stopping_distance="", max_towing="", height_modes=""):
        super().__init__(color, year, hp, speed_limit, mpg)
        self.stopping_distance = stopping_distance
        self.max_towing = max_towing
        self.height_modes = height_modes

    def create_truck(self):
        self.create_vehicle()
        self.stopping_distance = input("Enter Truck's Stopping Distance: ")
        self.max_towing = input("Enter Truck's Maximum Towing: ")
        self.height_modes = input("Enter Truck's Height Modes: ")

    def display(self):
        super().display()
        print("Truck's Stopping Distance:", self.stopping_distance)
        print("Truck's Max Towing:", self.max_towing)
        print("Truck's Height Modes:", self.height_modes)


class TowTruck(Truck):
    def __init__(self, color="", year="", hp="", speed_limit="", mpg="", stopping_distance="", max_towing="", height_modes="", towing_capacity="", curb_weight="", hitch_weight=""):
        super().__init__(color, year, hp, speed_limit, mpg, stopping_distance, max_towing, height_modes)
        self.towing_capacity = towing_capacity
        self.curb_weight = curb_weight
        self.hitch_weight = hitch_weight

    def create_tow_truck(self):
        self.create_truck()
        self.towing_capacity = input("Enter Tow Truck's Capacity: ")
        self.curb_weight = input("Enter Tow Truck's Curb Weight: ")
        self.hitch_weight = input("Enter Tow Truck's Hitch Weight: ")

    def display_tow_truck(self):
        super().display()
