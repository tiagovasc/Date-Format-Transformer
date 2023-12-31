from datetime import datetime, timedelta
import re

def parse_time(entry):
    now = datetime.now()
    parts = re.findall(r'(\d+)\s*(days|hrs|min)', entry)
    delta = timedelta()
    
    for amount, unit in parts:
        if unit == 'days':
            delta += timedelta(days=int(amount))
        elif unit == 'hrs':
            delta += timedelta(hours=int(amount))
        elif unit == 'min':
            delta += timedelta(minutes=int(amount))
    
    time_of_entry = now - delta
    return time_of_entry.strftime('%Y-%m-%d %H:%M:%S')

def main():
    with open('data.txt', 'r') as file:
        data = file.readlines()
    
    converted_data = [parse_time(entry.strip()) for entry in data]
    
    for entry in converted_data:
        print(entry)

if __name__ == '__main__':
    main()
