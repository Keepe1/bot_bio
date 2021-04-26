from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text
import DNK

@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
	await message.answer('Какая ваша цепочка ?',
reply_markup=menu)

@dp.message_handler(text="DNK")
async def show_dnk(message: Message):
	await message.answer('Вы выбрали Днк\nведите цепь Днк через: "-"\n(Нуклеотиды: A, T, C, G',
reply_markup=ReplyKeyboardRemove())
	
	@dp.message_handler(content_types=["text"])
	async def dnk_priom(message: Text):
		await message.answer(a = DNK.final(message))


@dp.message_handler(text="TRNK")
async def show_trnk(message: Message):
	await message.answer("Вы выбрали TRNK",
reply_markup=ReplyKeyboardRemove())
