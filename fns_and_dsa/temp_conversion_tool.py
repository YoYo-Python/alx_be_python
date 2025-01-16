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
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            
            if unit == 'C':
                converted_temperature = convert_to_fahrenheit(temperature)
                original_unit = 'F'
                print(f"{temperature:.1f}°C is {converted_temperature:.1f}°{original_unit}")
            elif unit == 'F':
                converted_temperature = convert_to_celsius(temperature)
                original_unit = 'C'
                print(f"{temperature:.1f}°F is {converted_temperature:.1f}°{original_unit}")
            else:
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
            
            break
        except ValueError:
            print("Invalid Temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

