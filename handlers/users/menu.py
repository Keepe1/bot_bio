from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
	await message.answer('Какая ваша цепочка ?',
reply_markup=menu)

@dp.message_handler(text="DNK")
async def show_dnk(message: Message):
	await message.answer("Вы выбрали DNK",
reply_markup=ReplyKeyboardRemove())
	@dp.message_handler()
	async def dnk_priom(message):
		await message.answer('working')


@dp.message_handler(text="TRNK")
async def show_trnk(message: Message):
	await message.answer("Вы выбрали TRNK",
reply_markup=ReplyKeyboardRemove())
