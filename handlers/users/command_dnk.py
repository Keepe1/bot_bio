import DNK
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

class DataInput(StatesGroup):
    r = State()

@dp.message_handler(commands=["DNK"])
async def show_dnk(message: Message):
	await message.answer('Вы выбрали Днк\nведите цепь Днк через: "-"\n(Нуклеотиды: A, T, C, G)',
reply_markup=ReplyKeyboardRemove())
	await DataInput.r.set()
	
	@dp.message_handler(state=DataInput.r) 
	async def dnk_priom(message: types.Message, state: FSMContext):
		r = message.text
		await message.answer(DNK.final(r))
		await state.finish()