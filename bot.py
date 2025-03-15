import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


TOKEN = 7436427585:AAGLZu8wowQMwBvVENmSVWSSBZ6VIEYQxpg



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


training_options = {
    "дупу": ["Ти присів 10 разів!", "Підкачав дупу на 5%", "Дупа стала ще соковитішою!"],
    "цицьки": ["Віджався 15 разів!", "Груди стали міцнішими!", "Тепер у тебе +2 до розміру!"],
    "член": ["Зробив 20 вправ на витривалість!", "Член збільшився на 0.5 см!", "Прокачка успішна!"]
}


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Дупу", "Цицьки", "Член"]
    keyboard.add(*buttons)
    await message.answer("Що будемо качати сьогодні? 😏", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text.lower() in training_options)
async def train(message: types.Message):
    category = message.text.lower()
    response = random.choice(training_options[category])
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
