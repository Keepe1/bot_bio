from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import DNK
import TRNK
from aiogram.dispatcher.filters import Command, Text
from keyboards.default import menu
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!Это бот \
    который поможет тебе с биологией .\
    Он может переводить Нуклеотиды в днк ( в данной версии нету штрихов и тд)\
    , так же он может решать генетические задачи с генами двух родителей. ")