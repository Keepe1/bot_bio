def task(a):
    #длиный перевод списков приводящий их к нужному состоянию для дальнейшей обработки  
    raw_data = list((a).split(" "))

    
    len_data = len(a)


    if len_data == 5:
        man_gen = list(raw_data[0])
        wom_gen = list(raw_data[1])

        two_gen_str = man_gen[0] + ":" + man_gen[1] + ":" + wom_gen[0] + ":" + wom_gen[1]

        two_gen = list(set(list((two_gen_str).split(":"))))

        verified_gen = []#список в который выходит отсортированый список (в формате AaBb)

        #Алгоритм для сортировки (в формате Aa)
        for i in (two_gen):
            for x in (two_gen):
                #промежуточные списки
                sort_a = []
                sort_list = []

            

                #перевод списков приводящий их к нужному состоянию для дальнейшей обработки  
                i = list(i)
                x = list(x)


                sort_a.append(str(i[0]))
                sort_a.append(str(x[0]))
                
                
                #промежуточные списки
                a=[]
                A=[]
                
                #Сортировка по велечине первой буквы 
                for y in sort_a:
                    if y == 'A':
                        A.append('A')
                    elif y =='a':
                        a.append('a')
                
                sort_list.append(''.join(A))
                sort_list.append(''.join(a))


                verified_gen.append(''.join(sort_list))
        
        #промежуточные списки
        counted_gen = []


        #обработка в ходе кторой дубликаты складываються 
        for i in verified_gen:
            repeat_gen = []

            for y in verified_gen:

                if i == y:
                    repeat_gen.append(y)
            
            if 2 <= len(repeat_gen):
                len_gen = len(repeat_gen)
                k = (f'{len_gen}{i}')

                counted_gen.append(k)
            
            else:
                counted_gen.append(i)


        counted_set_gen = ':'.join(set(counted_gen))

        #финальный список
        x = ('Варианты генотипов первого поколения: {0}'.format(counted_set_gen))
        #print(counted_set_gen)
        return x


    
    elif len_data == 9:
        man_gen = list(raw_data[0])
        wom_gen = list(raw_data[1])


        man_two_gen_str = man_gen[0] + man_gen[2] + ":" + man_gen[1] + man_gen[3] + \
        ":" + man_gen[0] + man_gen[3] + ":" + man_gen[1] + man_gen[2]
        wom_two_gen_str = wom_gen[0] + wom_gen[2] + ":" + wom_gen[1] + wom_gen[3] + \
        ":" + wom_gen[0] + wom_gen[3] + ":" + wom_gen[1] + wom_gen[2]


        man_two_gen = list(set(list((man_two_gen_str).split(":"))))
        wom_two_gen = list(set(list((wom_two_gen_str).split(":"))))
        
        #проверка на то чья цепочка генов длинее
        if len(man_two_gen) >= len(wom_two_gen):
            many_gen = (man_two_gen)
            few_gen = (wom_two_gen)

        else:
            many_gen = (wom_two_gen)
            few_gen = (man_two_gen)


        #print("many {0}".format(many_gen))

        verified_gen = []#список в который выходит отсортированый список (в формате AaBb)

        #Алгоритм для сортировки (в формате AaBb)
        for i in (many_gen):
            for x in (few_gen):
                #промежуточные списки
                sort_a = []
                sort_b = []
                sort_list = []

            

                #перевод списков приводящий их к нужному состоянию для дальнейшей обработки  
                i = list(i)
                x = list(x)


                sort_a.append(str(i[0]))
                sort_a.append(str(x[0]))
                

                
                sort_b.append(str(i[1]))
                sort_b.append(str(x[1]))
                
                #промежуточные списки
                a=[]
                A=[]
                
                #Сортировка по велечине первой буквы 
                for y in sort_a:
                    if y == 'A':
                        A.append('A')
                    elif y =='a':
                        a.append('a')
                
                sort_list.append(''.join(A))
                sort_list.append(''.join(a))

                #промежуточные списки
                b=[]
                B=[]
            
                #Сортировка по велечине первой буквы 
                for c in sort_b:
                    if c == 'B':
                        B.append('B')
                    elif c =='b':
                        b.append('b')
                
                sort_list.append(''.join(B))
                sort_list.append(''.join(b))
                


                verified_gen.append(''.join(sort_list))
                
        #print(verified_gen)

        #промежуточные списки
        counted_gen = []


        #обработка в ходе кторой дубликаты складываються 
        for i in verified_gen:
            repeat_gen = []

            for y in verified_gen:

                if i == y:
                    repeat_gen.append(y)
            
            if 2 <= len(repeat_gen):
                len_gen = len(repeat_gen)
                k = (f'{len_gen}{i}')

                counted_gen.append(k)
            
            else:
                counted_gen.append(i)


        counted_set_gen = ':'.join(set(counted_gen))

        #финальный список
        x = ('Варианты генотипов первого поколения: {0}'.format(counted_set_gen))
        #print(counted_set_gen)
        return x
