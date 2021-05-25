from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="/DNK"),
			KeyboardButton(text="/TRNK")
		],
		
	],
	resize_keyboard=True
)