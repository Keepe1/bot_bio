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
    await state.finish()

