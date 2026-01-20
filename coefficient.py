
""" op = operation; exe = execute

    python calculator
    allows user to execute one of four basic
    arithmetic ops with numbers.
    number can have floating point and/or negative value

    tg @shulepok
"""

coeff_val = 2.1


def plus(func):
    def coeff(op):
        if op == '=':
            print(f'{func('=')} + {coeff_val} = {func('=') + coeff_val}')
        else:
            func(op)
    return coeff


def minus(func):
    def coeff(op):
        if op == '=':
            print(f'{func('=')} - {coeff_val} = {func('=') - coeff_val}')
        else:
            func(op)
    return coeff


operations = ['+', '-', '*', '/', '='] # list of available operatons
num = 0.0 # main variable we will be forking with

def start_enter_num():
    """user enters that number at the beginning"""
    try:
        global num
        num = float(input('Enter the number: '))
    except ValueError:
        print('Услышал тебя, родной')
        start_enter_num()


def choose_op():
    """user can choose any one of four ops"""
    input_command = input(f'Enter the operation {operations}: ')
    if input_command in operations:
        return input_command
    else:
        print('Allowed operations -', operations)
        choose_op()

@plus
def executing_op(op):
    """and here user can exe operation that he want
       to execute with two numbers"""
    global num
    if op == '=':
        print(num)
        return num
    else:
        yanum = float(input('Another num: '))
        if op == '-':
            num -= yanum
        elif op == '*':
            num *= yanum
        elif op == '/':
            num /= yanum
        elif op == '+':
            num += yanum
        else:
            print('🤔')
        return num

"""main while that allows user to exe many operations
   with more than one number"""
start_enter_num()
while True:
    try:
        executing_op(choose_op())
    except KeyboardInterrupt:
        print('Executing was interrupted by user')
