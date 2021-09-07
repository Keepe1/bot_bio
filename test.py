def task(a):

    raw_data = list((a).split(" "))


    man_gen = list(raw_data[0])
    wom_gen = list(raw_data[1])


    man_two_gen_str = man_gen[0] + man_gen[2] + ":" + man_gen[1] + man_gen[3] + \
    ":" + man_gen[0] + man_gen[3] + ":" + man_gen[1] + man_gen[2]
    wom_two_gen_str = wom_gen[0] + wom_gen[2] + ":" + wom_gen[1] + wom_gen[3] + \
    ":" + wom_gen[0] + wom_gen[3] + ":" + wom_gen[1] + wom_gen[2]


    man_two_gen = list(set(list((man_two_gen_str).split(":"))))
    wom_two_gen = list(set(list((wom_two_gen_str).split(":"))))
    

    if len(man_two_gen) >= len(wom_two_gen):
        many_gen = (man_two_gen)
        few_gen = (wom_two_gen)

    else:
        many_gen = (wom_two_gen)
        few_gen = (man_two_gen)


    #print("many {0}".format(many_gen))

    verified_gen = []

    for i in (many_gen):
        for x in (few_gen):
            sort_a = []
            sort_b = []
            sort_list = []

        


            i = list(i)
            x = list(x)


            sort_a.append(str(i[0]))
            sort_a.append(str(x[0]))
            

            
            sort_b.append(str(i[1]))
            sort_b.append(str(x[1]))
            

            a=[]
            A=[]
            

            for y in sort_a:
                if y == 'A':
                    A.append('A')
                elif y =='a':
                    a.append('a')
            
            sort_list.append(''.join(A))
            sort_list.append(''.join(a))

            b=[]
            B=[]
        

            for c in sort_b:
                if c == 'B':
                    B.append('B')
                elif c =='b':
                    b.append('b')
            
            sort_list.append(''.join(B))
            sort_list.append(''.join(b))
            


            verified_gen.append(''.join(sort_list))
            
    #print(verified_gen)


    counted_gen = []

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
    x = ('Варианты генотипов первого поколения: {0}'.format(counted_set_gen))
    #print(counted_set_gen)
    return x

