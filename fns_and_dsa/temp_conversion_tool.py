# Define the constants for temperature conversion
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f'Temperature is {celsius:.2f}°C')

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f'Temperature is {fahrenheit:.2f}°F')

# Main code to take user input
temp = input("Enter the temperature to be converted: ")
cel_or_fahr = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Convert based on user input
if cel_or_fahr == 'C':
    convert_to_fahrenheit(temp)
elif cel_or_fahr == 'F':
    convert_to_celsius(temp)
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
