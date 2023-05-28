from application.db.people import *
from application.salary import *
import datetime

def main():
    name = 'Anto'
    calculate_salary(name)
    get_employees(name)
    now = datetime.datetime.now()
    now_str = now.strftime("%H:%M:%S  %d-%m-%Y")
    print(now_str)

if __name__ == '__main__':
    main()