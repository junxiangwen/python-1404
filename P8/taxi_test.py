from car import Car
from taxi import Taxi

def main():
    taxi = Taxi("Prius 1", 100)
    taxi.current_fare_distance = 40
    print(taxi)

    print(taxi.get_fare())

    taxi.start_fare()
    taxi.current_fare_distance =100

    print(taxi)
    print(taxi.get_fare())

if __name__ == '__main__':
    main()
