FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
    return fahrenheit

def main():
    temp = input("Enter the temperature to be converted:")
    cel_or_fahr = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if cel_or_fahr == 'C':
        convert_to_fahrenheit(temp)
    elif cel_or_fahr == 'F':
        convert_to_celsius(temp)
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
