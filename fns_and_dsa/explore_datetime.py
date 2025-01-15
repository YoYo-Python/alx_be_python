from datetime import datetime


now = datetime.datetime.now()
def display_current_datetime():
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: "+ current_date)
    
    def calculate_future_date():
        wanted_days = int(input("Enter the number of days to add to the current date: "))
        future_date = now + datetime.timedelta(days=wanted_days)
        future_date = future_date.strftime("%Y-%m-%d")
        print(f'Future date is: {future_date}')
    calculate_future_date()


display_current_datetime()


