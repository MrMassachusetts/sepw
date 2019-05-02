import sys
import os
os.system('cls' if os.name == 'nt' else 'clear')

version = 1.0
print('Social-Engineering Passwordlist-Generator')
print('Version: ', version)
print('Do you want to use the Guided version (1) or type Raw input (2)?')
pws = [0, 1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 1234567890, 420, 96, 'Password', 'password', 'qwerty', 'admin', 'login', 'qwerty']
fc = input('SEPw> ')
if fc == '1':
    print('Leave the input field blank if you dont know something')
    print('Enter your victims first name')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter your victims last name')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter your victims birth-year')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter your victims birth-month (in numbers)')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter the name of the victims partner')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter the first name of the victims child')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter the first name of the victims best friend')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter the first name of the victims mother')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter the first name of the victims father')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter the first name of the victims brother/sister')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter the victims city')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter the name of the victims pet-name')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter your victims favourite sports-team')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter your victims favourite actor')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Enter your victims favourite musician')
    temp = input('SEPw> ')
    pws.append(temp)
    print('Do you want to add any custom strings? (Y/N)')
    yn = input('SEPw> ')
    if yn == 'Y':
        fora = ''
        print('Type custom string hit enter. If you want to exit, type \'EXIT\'')
        while fora != 'EXIT':
            fora = input('SEPw> ')
            if fora != 'EXIT':
                pws.append(fora)
            else:
                print('How should the passwordlist should be named?')
    elif yn == 'N':
        print('How should the passwordlist should be named?')
    fn = (input('SEPw> '))
    print(pws)
    count = 0
    f1 = open(fn, 'wt')
    for i in range(0, len(pws)):
        for a in range(0, len(pws)):
            if pws[i] == '' or pws[a] == '':
                print('Empty Param')
            else:
                pw = pws[i], pws[a], '\n'
                pw = ''.join(map(str, pw))
                print(pw)
                f1.write(pw)
                count = count + 1
    for i in range(0, len(pws)):
        temp = pws[i], '\n'
        temp = ''.join(map(str, temp))
        f1.write(temp)

    f1.close()
    print(count, ' possible passwords have been generated')
    print('The list has been generated. Press enter to exit')
    input('')
elif fc == '2':
    print('Enter your words, seperated by enter. If you are finished type \'EXIT\'')
    fora = ''
    while fora != 'EXIT':
        fora = input('SEPw> ')
        if fora != 'EXIT':
            pws.append(fora)
        else:
            print('How should the passwordlist should be named?')
    fn = (input('SEPw> '))
    print(pws)
    count = 0
    f1 = open(fn, 'wt')
    for i in range(0, len(pws)):
        for a in range(0, len(pws)):
            if pws[i] == '' or pws[a] == '':
                print('Empty Param')
            else:
                pw = pws[i], pws[a], '\n'
                pw = ''.join(map(str, pw))
                print(pw)
                f1.write(pw)
                count = count + 1
    for i in range(0, len(pws)):
        temp = pws[i], '\n'
        temp = ''.join(map(str, temp))
        f1.write(temp)

    f1.close()
    print(count, ' possible passwords have been generated')
    print('The list has been generated. Press enter to exit')
    input('')
else:
    sys.exit()
