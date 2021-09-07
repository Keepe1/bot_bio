from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove, message
from aiogram.dispatcher.filters import Command, Text
from states.task_vub import tvubor
from aiogram.dispatcher import FSMContext

import test


@dp.message_handler(Command('task_gen'))
async def show(message: Message):
    await message.answer("Введите гены родителей (AaBb AaBb)")
    await tvubor.F1.set()

@dp.message_handler(Message, state = tvubor.F1)
async def answer_f1(message: Message, state: FSMContext):
    answer = message.text
    
    await message.answer(test.task(answer))

    await state.update_data(answer1 = answer)
    await tvubor.next()

@dp.message_handler(state=tvubor.F2)
async def show(message: Message, state: FSMContext):
    chain = message.text
    data = await state.get_data()
    answer1 = data.get("answer1")
    await message.answer(':)')
    await state.finish()