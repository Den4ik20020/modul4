class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee


employees = [
    Employee('Никита', 200_000, "vacation", True),
    Employee('Стёпа', 200_000, "vacation", True),
    Employee('Данил', 200_000, "vacation", False),
    Employee('Юра', 200_000, "vacation", True),
    Employee('Глеб', 200_000, "vacation", True),
]


for employee in employees:

    if not employee.is_good_employee:
        employees.remove(employee)
