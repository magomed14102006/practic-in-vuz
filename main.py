from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7304813007:AAEHQBj0r4CxvGyIbzH7adxGgf1cs62Sse8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Обратная связь', url='t.me/nemeowtoday'))
    markup.add(types.InlineKeyboardButton('Информация', callback_data='И тут тоже не придумал('))
    markup.add(types.InlineKeyboardButton(text='Сайт', web_app=WebAppInfo(url='https://doyouwannagooutwithmaga.netlify.app/')))
    await message.reply('Привет, зайди на сайт.', reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


executor.start_polling(dp)
