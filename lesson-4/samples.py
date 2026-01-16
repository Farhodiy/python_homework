while True:
    a=int(input('a='))
    b=int(input('b='))

    operation = input('choose:(+,-,*,/)')
    if operation == '+':
        print('a+b=',a+b)

    elif operation == '-':
        print('a-b',a-b)
    elif operation == '*':
        print('a*b=',a*b)
    elif operation == '/':
        print('a/b=',a/b)
    q=input('Do you want to continue?')
    if q.lower() in ['q','quit','no','n']:
        break