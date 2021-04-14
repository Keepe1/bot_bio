a = input('Какая ваша цепочка (DNK, tRNK,)?' )

def TRNK(x):
    if x == 'A':
        x = 'U'
        return x
    if x == 'T':
        x = 'A'
        return x
    if x == 'C':
        x = 'G'
        return x
    if x == 'G':
        x == 'C'
        return x


if a == 'DNK':
    #ввод данных
    dnk = list(map(str, input('Введите 5 алелей ДНК (через) - ').split('-')))
    
    #алели
    A1 = list(str(dnk[0]))
    A2 = list(str(dnk[1]))
    A3 = list(str(dnk[2]))
    A4 = list(str(dnk[3]))
    A5 = list(str(dnk[4]))
    
    #нуклеотиды
    nukl1 = A1[0]
    nukl2 = A1[1]
    nukl3 = A1[2]

    nukl4 = A2[0]
    nukl5 = A2[1]
    nukl6 = A2[2]

    nukl7 = A3[0]
    nukl8 = A3[1]
    nukl9 = A3[2]
    
    nukl10 = A4[0]
    nukl11 = A4[1]
    nukl12 = A4[2]

    nukl13 = A5[0]
    nukl14 = A5[1]
    nukl15 = A5[2]

    #реализация функции
    sec_nukl1 = TRNK(nukl1)
    sec_nukl2 = TRNK(nukl2)
    sec_nukl3 = TRNK(nukl3)

    sec_nukl4 = TRNK(nukl4)
    sec_nukl5 = TRNK(nukl5)
    sec_nukl6 = TRNK(nukl6)

    sec_nukl7 = TRNK(nukl7)
    sec_nukl8 = TRNK(nukl8)
    sec_nukl9 = TRNK(nukl9)
    
    sec_nukl10 = TRNK(nukl10)
    sec_nukl11 = TRNK(nukl11)
    sec_nukl12 = TRNK(nukl12)

    sec_nukl13 = TRNK(nukl13)
    sec_nukl14 = TRNK(nukl14)
    sec_nukl15 = TRNK(nukl15)
    
    trnk = sec_nukl1 + sec_nukl2 + sec_nukl3 + '-' + sec_nukl4 + sec_nukl5 +\
    sec_nukl6 + '-' + sec_nukl7 + sec_nukl8 + sec_nukl9 + '-' + sec_nukl10 +\
    sec_nukl11 + sec_nukl12 + '-' + sec_nukl13 + sec_nukl14 + sec_nukl15

    print(trnk)