import os

def get_user_input():
    name = input('Введіть своє ім`я: ')
    if name.strip():
        print('Ваше ім`я дійсне')
    else:
        print('Ваше ім`я не дійсне')
    month = int(input('Введіть місяць народження (цифрою): '))
    year = int(input('Введіть рік народження: '))
    return name, month, year

def validate_month(month):
    if month < 1 or month > 12:
        print('Місяць введено неправильно!')

def validate_year(year):
    if year < 1 or year > 120:
        print('Рік введено неправильно!')

def create_test_file(name, month, year):
    with open('textttt.txt', 'a') as file:
        file.write(f'Ім`я: {name}\n')
        file.write(f'Місяць: {month}\n')
        file.write(f'Рік: {year}\n')

user_input = get_user_input()
validate_month(user_input[1])
validate_year(user_input[2])
create_test_file(*user_input)

