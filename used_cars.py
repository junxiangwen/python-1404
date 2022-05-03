"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("limo",100,115)
    my_car.add_fuel(20)
    my_car.drive(115)
    print(my_car)




main()
