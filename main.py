from application.db.people import get_employees
from application.salary import calculate_salary
import datetime

def main():
    name = 'Anton'
    calculate_salary(name)
    get_employees(name)
    now = datetime.datetime.now()
    now_str = now.strftime("%H:%M:%S  %d-%m-%Y")
    print(now_str)

if __name__ == '__main__':
    main()