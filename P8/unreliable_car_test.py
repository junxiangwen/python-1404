from car import Car
from unreliable_car import Unreliable

def main():
    unreliable = Unreliable("xxx", 100, 0)
    unreliable.drive(40)
    print(unreliable)
    if unreliable.reliability > unreliable.drive(40):
        print("can drive")
    else:
        print(" can not drive")
if __name__ == '__main__':
    main()
