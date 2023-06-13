employee = {
    'name': 'Дмитрий',
    'salary': 350_000,
    'age': 16,
}

print(employee)

employee['name'] = 'Валера'

print(employee)

print(employee.get('name'),employee.get('salary'), employee.get('age'))
