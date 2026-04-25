from calculator import add, subtract, multiply, divide

history = []

def show_menu():
    print("\n=== CLI Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show history")
    print("6. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Goodbye.")
            break

        if choice == "5":
            if not history:
                print("No calculations yet.")
            else:
                print("\n=== History ===")
                for entry in history:
                    print(entry)
            continue

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid option. Please choose from 1 to 5.")
            continue

        first_number = get_number("Enter first number: ")
        second_number = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = add(first_number, second_number)
            elif choice == "2":
                result = subtract(first_number, second_number)
            elif choice == "3":
                result = multiply(first_number, second_number)
            elif choice == "4":
                result = divide(first_number, second_number)

            print(f"Result: {result}")
            operation_map = {
                "1": "+",
                "2": "-",
                "3": "*",
                "4": "/"
            }

            history.append(f"{first_number} {operation_map[choice]} {second_number} = {result}")dir

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
