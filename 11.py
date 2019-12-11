
what = input('Что делаем?(+,-,/,*): ')

a= float (input('введи число A: '))
b= float(input ('Введи число B: '))

if what == '+':
    c = a + b
    print('Результат: ' + str(c))
    
elif what == '-':
    c = a - b
    print('Результат: ' + str(c))
    
elif  what == '/':
    c = a / b
    print('Результат: ' + str(c))
    
elif what == '*':
    c = a * b
    print('Результат: ' + str(c))
    
else:
    print('Выбрано не верное действие!')