from car import Car

class Unreliable(Car):

    def __init__(self, car_name, fuel, reliability):
        Car.__init__(self, car_name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"car:{self.car_name},fuel={self.fuel},reliability={self.reliability}"

    def drive(self, distance):
        import random
        number = random.randint(1, 100)
        return number


