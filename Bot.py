import logging
import config

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
	if message == 'dnk':
		text = 'working'
		await message.answer(text=text)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
