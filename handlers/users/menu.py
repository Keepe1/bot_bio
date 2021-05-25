from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text
import TRNK
import DNK

@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
	await message.answer('Какая ваша цепочка ?',
reply_markup=menu)


@dp.message_handler(commands=["TRNK"])
async def show_trnk(message: Message):
	await message.answer("Вы выбрали TRNK",
reply_markup=ReplyKeyboardRemove())
	t = "trnk_type"
		

@dp.message_handler(commands=["DNK"])
async def show_dnk(message: Message):
	t = "dnk_type"


	await message.answer('Вы выбрали Днк\nведите цепь Днк через: "-"\n(Нуклеотиды: A, T, C, G)',
reply_markup=ReplyKeyboardRemove())

	

@dp.message_handler() 
async def dnk_priom(message: Message):
	await message.answer(t)
	r = message.text
	if t == 'dnk_type':
		await message.answer(DNK.final(r))
	elif t == 'trnk_type':
		await message.answer(TRNK.final(r))
