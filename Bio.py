
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
    elif a == 'UUA' or a == 'UUG' or a == 'CUU'\
    or a == 'CUC' or a == 'CUA' or a == 'CUG':
        amin.append('leucine')
    elif a == 'UCU' or a == 'UCC' or a == 'UCA' or a == 'UCG':
        amin.append('serine')
    elif a == 'UAU' or a == 'UAC':
        amin.append('tyrosine')
    elif a == 'UAA' or a == 'UAG' or a == 'UGA':
        amin.append('stop-codon')
    elif a == 'UAU' or a == 'UAC':
        amin.append('cysteine')
    elif a == 'UGG':
        amin.append('tryptophan')
    elif a == 'CCU' or a == 'CCC' or a == 'CCA' or a == 'CCG':
        amin.append('proline')
    elif a == 'CAU' or a == 'CAC':
        amin.append('histidine')
    elif a == 'CAA' or a == 'CAG':
        amin.append('glumatin')
    elif a == 'CGU' or a == 'CGC' or a == 'CGA' or a == 'CGG'\
    or a == 'AGA' or a == 'AGG':
        amin.append('arginine')
    elif a == 'AUC' or a == 'AUU' or a == 'AUA':
        amin.append('isoleucine')
    elif a == 'AUG':
        amin.append('methionine')
    elif a == 'ACU' or a == 'ACC' or a == 'ACA' or a == 'ACG':
        amin.append('threonine')
    elif a == 'AAU' or a == 'AAC':
        amin.append('asparagine')
    elif a == 'AAA' or a == 'AAG':
        amin.append('lysine')
    elif a == 'AGU' or a == 'AGC':
        amin.append('serine')
    elif a == 'GUU' or a == 'GUA' or a == 'GUC' or a == 'GUG':
        amin.append('valine')
    elif a == 'GCU' or a == 'GCC' or a == 'GCA' or a == 'GCG':
        amin.append('alanine')
    elif a == 'GAU' or a == 'GAC':
        amin.append('aspartic acid')
    elif a == 'GAA' or a == 'GAG':
        amin.append('glutamic acid')
    elif a == 'GGU' or a == 'GGA' or a == 'GGC' or a == 'GGG':
        amin.append('glycine')


def find_stop_codon(acid):
    for i in acid:
        if i == 'stop-codon':
            break
        else:
            final_acid.append(i)


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
                    
                    amin = []#список для функции превода нуклеотидов ирнк в кислоты

                    three_operator = list(map(AMIN, n))#перевод днк в иРНК

                    final_acid = []
                    find_stop_codon(amin)
                    print(final_acid)


            else:
                print('Введено не верное значение')
                break
    elif question == "/end":
                print('Заверешение работы')
                break
    else:
        print('Error')
