from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="/register")
    return builder.as_markup()