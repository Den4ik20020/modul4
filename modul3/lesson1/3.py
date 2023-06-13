employee_list = [
    {
        'name': 'Валерий',
        'salary': 200,
        'age': 4,
    },
    {
        'name': 'Денис',
        'salary': 20,
        'age': 16,
    },
    {
        'name': 'Дмитрий',
        'salary': 0,
        'age': 15,
    }
]

for employee in employee_list:
    print(employee.get('name'))

del employee_list[-1]
print(employee_list)
