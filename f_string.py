def print_name(message) -> None:
    print(message)

def name_input() -> str:
    try:
        name = input('Your name: ')
        if not name:
            raise ValueError('Name cannot be empty')
        assert 2 <= len(name) <= 50, 'Name\'s length must be grater then 2 symbols and less then 50 symbols'
    except ValueError as e:
        print(e)
        #raise(e)
    except AssertionError as e:
        print(e)
        #raise(e)
    else:    
        return name
    return 0

def age_input() -> int:
    max_input_iter = 3
    current_iter = 0

    while current_iter < max_input_iter:
        try:
            age = int(input('Your age: '))
            assert 1 <= age <= 150, 'Age must be round number in range from 1 to 150'
        except ValueError as e:
            raise(e)
        return age

max_input_iter = 3
current_iter = 0
while current_iter < max_input_iter:
    name = name_input()

    if name:
        break
    elif current_iter == 2:
        print('You have exceeded the number of input attempts')
        break
    else:
        current_iter += 1
        
age = age_input()

message = (
        f'Hello, {name}. \n'
        f'You are {age} age old. '
)

print_name(message)

