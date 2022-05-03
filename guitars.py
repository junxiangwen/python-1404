from guitar import Guitar




def main():
    guitars = []
    print("My guitars!")
    done = 0
    while done != " ":
        name = input("Name:")
        year = input("Year:")
        cost = input("Cost:$")
        guitars.append(Guitar(name, year, cost))
        print("{} ({}):$ {} added.".format(name, year, cost))
    else:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}"),(" (vintage)" if 2021-int(guitar.year) > 50 else " ")


main()
