import os
import time
import shutil


# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source_1 = list(map(str, input('Введите путь для папки с копируемыми фалами  - ').split( '\ ' )))
source = str("\\".join(source_1))
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\\backup'
# Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
today = target_dir + os.sep + time.strftime('%Y.%m.%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H.%M.%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий -->')
if len(comment) == 0:# проверяем, введён ли комментарий
	target = today + os.sep  + now
else:
	target = today + os.sep + now + '_' +\
	comment.replace(' ','_')

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
	os.mkdir(today)# создание каталога
print('Каталог успешно создан', today)
 

shutil.make_archive(target, 'zip', source)

# Запускаем создание резервной копии
if os.path.exists(target) == False :
	print('Резервная копия успешно создана в', target)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')
