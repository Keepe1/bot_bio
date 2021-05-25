import DNK

H = input()

g=DNK.final(H)
print(g)

x=50
def func():
	global x
	
	print('x равно',x)
	x=2
	print('Заменяем глобальное значение x на',x)
func()
print('Значение x составляет', x)