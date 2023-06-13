age = 17

if age >= 18:
    is_allow = 'Можно'
else:
    is_allow = 'Нельзя'

citizenship = 'РФ'
is_allow = 'Можно' if age >=18 or citizenship == 'РФ' else 'Нельзя'
print(is_allow)
