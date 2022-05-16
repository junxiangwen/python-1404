

from silver_service_taxi import Silver_Service_Taxi


def main():
    taxi = Silver_Service_Taxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()
