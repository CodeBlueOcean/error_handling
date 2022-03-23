# Error Handling

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('something is wrong' + err)


print(sum(1,'2'))


# Error Handling (this is an error object)

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('something is wrong' + err)


print(sum(1,'2'))

# Error Handling (this is an error object) it is a built-in exception of python. you want to use a f string

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter numbers {err}')

# Error Handling  ex

def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError): 
        print(sum(1, 0))

# Error Handling  ex

def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err: 
        print(err)

print(sum(1,'2'))


