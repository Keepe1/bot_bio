raw_data = list(input("вводи фигню").split(" "))
print(raw_data)

man_gen = list(raw_data[0])
wom_gen = list(raw_data[1])
print(man_gen)
print(man_gen[0])

man_two_gen_str = man_gen[0] + man_gen[2] + ":" + man_gen[1] + man_gen[3] + \
":" + man_gen[0] + man_gen[3] + ":" + man_gen[1] + man_gen[2]
wom_two_gen_str = wom_gen[0] + wom_gen[2] + ":" + wom_gen[1] + wom_gen[3]
print(man_two_gen_str)

man_two_gen = list((man_two_gen_str).split(":"))
wom_two_gen = list((wom_two_gen_str).split(":"))
print(man_two_gen)

man_two_gen = list(set(man_two_gen))
print(man_two_gen)
man_two_gen.sort()
print(man_two_gen)


#man_two_gen = list(''.join(man_two_gen))
#print(man_two_gen)

#man_two_gen.sort(key=str.upper)
#print(man_two_gen)

