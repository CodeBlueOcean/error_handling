#Error Handling

while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except:
        print('please enter a number')
    else:
        print('thank you!')
        break


#Error Handling

while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you!')
        break
    

    

