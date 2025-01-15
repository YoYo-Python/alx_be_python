FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    celsius = float(fahrenheit) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f'Tempreture is {celsius}°C')

def convert_to_fahrenheit(celsius):
    fahreheit = float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f'Tempreture is {fahreheit}°F')

temp = input("Enter the tempreture to be converted: ")
cel_or_fahr = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if cel_or_fahr == 'C':
    convert_to_celsius(temp)
elif cel_or_fahr == 'F':
    convert_to_fahrenheit(temp)

