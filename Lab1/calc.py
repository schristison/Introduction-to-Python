# method on the top
def separator():
    print(60 * '-')

def menu():
    print(2 * '\n') # \n means empty lines
    separator()
    print('Welcome to PyCalc')
    separator()

    print('[1] - Add')
    print('[2] - Subtract')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Exit')


# instructions on the bottom

opc = ''
while (opc != 'x'):
    menu()
    opc = input('Select an option: ')
    if(opc == 'x'):
        break # break finish with the loop

    num1 = float(input('First Number: '))
    num2 = float(input('Second Number: '))
    
    if(opc == '1'):
       res = num1 + num2
       print('Addition = ' + str(res))

    elif(opc == '2'):
        res = num1 - num2
        print('Subtraction = ' + str(res))

    elif(opc =='3'):
        res = num1 * num2
        print('Multiplication = ' + str(res))

    elif(opc == '4'):
        if(num2 == 0):
            print('Error: Dividing by 0 is not allowed')
        else:
            res = num1 / num2
            print('Division = ' + str(res))

    input('Press Enter to continue...')

    
    
print('Thanks very much!')