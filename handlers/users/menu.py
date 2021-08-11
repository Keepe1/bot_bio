from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text
import DNK
import TRNK
from states.vubor import vubor
from aiogram.dispatcher import FSMContext


@dp.message_handler(Command('translate'))
async def show_menu(message: Message):
	await message.answer('Какая ваша цепочка ?',
reply_markup=menu)
	await vubor.F1.set()


@dp.message_handler(Message, state = vubor.F1)
async def answer_f1(message: Message, state: FSMContext):
	answer = message.text
	
	if answer == "DNK":
		await message.answer('Вы выбрали Днк\nведите цепь Днк через: "-"\n(Нуклеотиды: A, T, C, G)')
	elif answer == "TRNK":
		await message.answer('Вы выбрали тРНК\nведите цепь Днк через: "-"\n(Нуклеотиды: A, U, C, G)')
	
	await state.update_data(answer1 = answer)
	await vubor.next()


@dp.message_handler(state=vubor.F2)
async def show(message: Message, state: FSMContext):
	chain = message.text
	data = await state.get_data()
	answer1 = data.get("answer1")
	
	if answer1 == 'DNK':
		await message.answer(DNK.final(chain))

	elif answer1 == 'TRNK':
		await message.answer(TRNK.final(message.text))

	await state.finish()
