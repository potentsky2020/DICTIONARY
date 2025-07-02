def main():
    name, house = get_student()
    print(f"Hello, {name} from {house}!")

def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return name, house


if __name__ == "__main__":
    main()
