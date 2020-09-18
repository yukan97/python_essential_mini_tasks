class Vehicle:
    def __init__(self, engine, speed):
        self.engine = engine
        self.speed = speed
    
    def print_attr(self):
        print(self.__class__.__name__, self.engine, self.speed)
    
class LandVehicle(Vehicle):
    def __init__(self, engine, speed, trunk_size, max_passangers):
        super().__init__(engine, speed)
        self.trunk_size = trunk_size
        self.max_passangers = max_passangers
        
    def print_attr(self):
        print(f"{self.__class__.__name__}, engine: {self.engine}, " +
              f"speed: {self.speed}, trunk_size: {self.trunk_size}, " +
              f"max no of passangers: {self.max_passangers}")
        
class AirCraft(Vehicle):
    def __init__(self, engine, speed, wings_width, max_hight):
        super().__init__(engine, speed)
        self.wings_width = wings_width
        self.max_hight = max_hight
        
    def print_attr(self):
        print(f"{self.__class__.__name__}, engine: {self.engine}, " +
              f"speed: {self.speed}, wings_width: {self.wings_width}, " +
              f"max_hight: {self.max_hight}")
        
class NavyVehicle(Vehicle):
    def __init__(self, engine, speed, ship_length, max_crew):
        super().__init__(engine, speed)
        self.ship_length = ship_length
        self.max_crew = max_crew
    
    def print_attr(self):
        print(f"{self.__class__.__name__}, engine: {self.engine}, " +
              f"speed: {self.speed}, ship_length: {self.ship_length}, " +
              f"max_crew: {self.max_crew}")
        
car = LandVehicle('engine1', 320, 50, 4)
jet_plane = AirCraft('engine2', 800, 4, 2)
cruise_lainer = NavyVehicle('engine3', 300, 32, 11)

car.print_attr()
jet_plane.print_attr()
cruise_lainer.print_attr()
