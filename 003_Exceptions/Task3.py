class IncorrectYearException(Exception):
    pass

class Employee:
    
    def __init__(self, name, surname, department, start_date):
        
        if not(isinstance(name, str) and
               isinstance(surname, str) and
               isinstance(department, str)):
            raise TypeError('Name, surname and department should be string')
        elif start_date < 2000 or start_date > 2020:
            raise IncorrectYearException('Wrong year of employment')
        else:
            self.name = name
            self.surname = surname
            self.department = department
            self.start_date = start_date
    
    def __str__(self):
        return f"Employee ( {self.name}, {self.surname}, {self.department}, {self.start_date})"
    def __repr__(self):
        return f"Employee ( {self.name}, {self.surname}, {self.department}, {self.start_date})"

employees = [] 
i = 0;       
while i <= 2:
    data = input('Enter employee data separated by space ').split()
    i += 1 
    print(data)
    try:
        employee = Employee(data[0], data[1], data[2], int(data[3]))
        employees.append(employee)
    except TypeError as e1:
        print(e1)
    except IncorrectYearException as e2:
        print(e2)
    finally:
        print(employees)