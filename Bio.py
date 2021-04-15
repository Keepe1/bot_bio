b = []
def TRNK(x):
    x = str(x)
    if x == 'A' or x == 'a': 
        b.append('U')
    elif x == 'T' or x == 't':
        b.append('A')
    elif x == 'C' or x == 'c':
        b.append('G')
    elif x == 'G' or x == 'g':
        b.append('C')
    elif x == '-':
        b.append('-')
    else:
        print('error')

while True:
    question = input('Для начала работы введите комманду - /start \nДля завершения работы введите комманду - /end:\n') 
    if question == "/start":
        while True:
            a = input('Какая ваша цепочка (DNK, tRNK,)?:\n' )
            if a == 'DNK' or a == 'dnk':
                
                #ввод данных
                dnk = list(input('Введите 5 алелей ДНК (через "-"):\n'))
                
                second_operator = list(map(TRNK, dnk))
                f = (''.join(b))
                print(f)
            else:
                print('Введено не верное значение')
                break
    elif question == "/end":
                print('Заверешение работы')
                break
    else:
        print('Error')