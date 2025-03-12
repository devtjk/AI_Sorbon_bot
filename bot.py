import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from openai import OpenAI

# Инициализация бота
API_TOKEN = '7133856476:*****'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация OpenAI
client = OpenAI(api_key="sk-proj-*****")

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я Сорбон, ваш ИИ помощник в учебе. Какой у Вас вопрос сегодня?")

@dp.message_handler()
async def echo(message: types.Message):
    # Отправка сообщения в LLM
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": message.text}
        ]
    )
    
    # Получение ответа и отправка его пользователю
    response = completion.choices[0].message['content']
    await message.reply(response)

if name == 'main':
    executor.start_polling(dp, skip_updates=True)