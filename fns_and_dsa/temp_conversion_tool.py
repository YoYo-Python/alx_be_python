# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    celsius = (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    fahrenheit = (float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    """
    Main function to interact with the user and perform temperature conversion.
    """
    try:
        # Prompt the user to enter a temperature
        temp = input("Enter the temperature to convert: ").strip()

        # Ensure the temperature input is numeric
        if not temp.replace('.', '', 1).isdigit() and not temp.replace('-', '', 1).replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # Prompt the user to specify the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the appropriate conversion based on the input unit
        if unit == 'F':
            result = convert_to_celsius(temp)
            print(f"{float(temp):.2f}°F is {result:.2f}°C")
        elif unit == 'C':
            result = convert_to_fahrenheit(temp)
            print(f"{float(temp):.2f}°C is {result:.2f}°F")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # Handle invalid temperature input
        print(e)

if __name__ == "__main__":
    main()
