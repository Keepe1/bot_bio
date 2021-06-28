class dnk:
  # Функция перевода нуклеотидов в ирнк(работает с трнк и с днк)
	def iRNK(self, nukl):
	    x = str(nukl)
	    if x == 'A' or x == 'a': 
	        irnk.append('U')
	    elif x == 'T' or x == 't' or x == 'U' or x == 'u':
	        irnk.append('A')
	    elif x == 'C' or x == 'c':
	        irnk.append('G')
	    elif x == 'G' or x == 'g':
	        irnk.append('C')
	    elif x == '-':
	        irnk.append('-')
	    else:
	        irnk.append('?')


	# функция превода в аминокислоты
	def AMIN(self, aleli):

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


	def find_stop_codon(self, acid):
	    for i in acid:
	        if i == 'stop-codon':
	            break
	        else:
	            final_acid.append(i)

d = dnk()
irnk = []
amin = []
final_acid = []

def final(nukl):
	dnk = list(nukl)
	
	#список для функции превода днк в ирнк
	
	second_operator = list(map(d.iRNK, dnk))
	#перевод днк в иРНК 

	irnk_str = str(''.join(irnk))
	#создание str строки из списка

	#создание списка триплетов
	irnk_list = irnk_str.split('-')

	
	#список для функции превода нуклеотидов ирнк в кислоты

	three_operator = list(map(d.AMIN, irnk_list))
	#перевод днк в иРНК

	
	d.find_stop_codon(amin)
	DNK = str(''.join(dnk))
	ACID = str(', '.join(final_acid))

	finish=('Ваша ДНК цепь: {0} \nВаша цепь иРНК: {1} \nВаша цепь аминокислот: {2}'.format(DNK, irnk_str, ACID))
	finish_out=finish
	if len(finish) > 0 :
		del irnk[:]
		del amin[:]
		del final_acid[:]
	return finish_out
