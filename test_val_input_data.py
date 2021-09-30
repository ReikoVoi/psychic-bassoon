import pytest
import re

def test_name_input() -> str:
    max_input_iter = 3
    current_iter = 0
    name = ''

    while current_iter < max_input_iter and not bool(name):
        try:
            name = input('Your name: ')
            regexp = '^([A-Z])([a-z]{2,30})$'
            if not re.match(regexp, name):
                raise ValueError('\nDo not match the format: \nName shouldn\' be empty.\nName should contain only letters. \nStarts from capital letter. \nName length should be within 2 and 30 symbols.\n')
            # if not name:
            #     raise ValueError('Name cannot be empty')
            # assert 2 <= len(name) <= 50, 'Name\'s length must be grater then 2 symbols and less then 50 symbols'
        except ValueError as e:
            print(e)
            #raise(e)
        # except AssertionError as e:
        #     print(e)
            #raise(e)
        else:    
            return name
        
        current_iter += 1
        name = ''

    if current_iter == max_input_iter:
        print('You have exceeded the number of input attempts')

def test_age_input() -> int:
    max_input_iter = 3
    current_iter = 0
    age = ''

    while current_iter < max_input_iter and not bool(age):
        try:
            age = input('Your age: ')
            if not age:
                raise ValueError('Age cannot be empty')
            age = int(age)
            assert 1 <= age <= 150, 'Age must be round number in range from 1 to 150'
        except AssertionError as e:
            print(e)
        except ValueError as e:
            print(e)
        else:
            return age

        current_iter += 1
        age = ''  

    if current_iter == max_input_iter:
        print('You have exceeded the number of input attempts')

name = test_name_input()
age = test_age_input()

print(f'Hello, {name}. \nYou are {age} age old.')

