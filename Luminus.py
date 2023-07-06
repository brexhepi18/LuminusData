def set_temp_value():
    while True:
        value = input("Set desired temperature (18° - 35°): ")
        try:
            temp_value = float(value)
            if 18 <= temp_value <= 35:
                print(f"Setting heating system temperature to: {temp_value}° ...")
                return 
            else:
                print("Invalid input. Value must be between 18 and 35.")
        except ValueError:
            print("Invalid input. Please enter a valid float value.")

def get_user_choice():
    while True:
        print("Please select an option:")
        print("1. Manual Mode")
        print("2. Auto Mode")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            set_temp_value()
        else:
            print("Invalid input. Please try again.")

# Usage example
user_choice = get_user_choice()
print("You selected option", user_choice)

