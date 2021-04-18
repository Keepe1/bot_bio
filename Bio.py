
# Функция перевода нуклеотидов
def iRNK(nukl):
    x = str(nukl)
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
        print('?')


# функция превода в аминокислоты
def AMIN(aleli):

    a = str(aleli)

    if a == 'UUU' or a == 'UUC':
        amin.append('phenylalanine')

    if a == 'UUA' or a == 'UUG' or a == 'CUU'\
    or a == 'CUC' or a == 'CUA' or a == 'CUG':
        amin.append('leucine')

    if a == 'UCU' or a == 'UCC' or a == 'UCA'\
    or a == 'UCG':
        amin.append('serine')


# сама зацикленная программа
while True:

    question = input('Для начала работы введите комманду - /start \nДля завершения работы введите комманду - /end:\n')
    
    #проверки на выполнение программы
    if question == "/start":
        
        #зацикливание процесса перевода нуклеотидов и аминокислот
        while True:
            
            a = input('Какая ваша цепочка (DNK, tRNK,)?:\n' )
            
            if a == 'DNK' or a == 'dnk':
                
                #ввод данных
                dnk = list(input('Введите 5 алелей ДНК (через "-"):\n'))
                b = []#список для функции превода днк в ирнк
                
                second_operator = list(map(iRNK, dnk))#перевод днк в иРНК 
                f = (''.join(b))#создание str строки из списка
                print(f)
                
                j = input('Переводим нуклеотиды?:\n' )

                if j == 'Y':
                    
                    #создание списка триплетов
                    n = f.split('-')
                    print(n)
                    
                    amin = []#список для функции превода нуклеотидов ирнк в кислоты

                    three_operator = list(map(AMIN, n))#перевод днк в иРНК
                    print(amin)

            else:
                print('Введено не верное значение')
                break
    elif question == "/end":
                print('Заверешение работы')
                break
    else:
        print('Error')
