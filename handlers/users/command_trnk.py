import TRNK
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

class DataInput(StatesGroup):
    r = State()

@dp.message_handler(commands=["TRNK"])
async def show_trnk(message: Message):
	await message.answer("Вы выбрали TRNK",
reply_markup=ReplyKeyboardRemove())
	await DataInput.r.set()

	@dp.message_handler(state=DataInput.r)
	async def trnk_priom(message: types.Message, state: FSMContext):
		r = message.text
		await message.answer(TRNK.final(r))
		await state.finish()