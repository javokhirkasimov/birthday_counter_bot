import logging
from calc_func import calculate_bdays
from aiogram import Bot, Dispatcher, executor, types
from environs import Env

env = Env()
env.read_env()


API_TOKEN = env.str('TOKEN')
STICKER_ID = env.str('STICKER_ID')

# Configure logging
logging.basicConfig(level=logging.INFO)

proxy_url = None

# proxy_url = 'http://proxy.server:3128'  # uncomment it to set proxy

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, proxy=proxy_url, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Assalomu Alaykum, menga tug'ilgan sanangizni <b>30.09.2001</b> ushbu formatda yuboring.")


@dp.message_handler(lambda msg: len(msg.text.split('.')) == 3)
async def send_birthday_info(message: types.Message):
    try:
        text = await calculate_bdays(message)
        await message.answer(text)
    except Exception as e:
        print(e)
        await message.answer("Iltimos tug'ilgan sanangizni to'g'ri formatda kiriting!")


@dp.message_handler(content_types='any')
async def send_sticker(message: types.Message):
    await message.answer_sticker(STICKER_ID)
    await message.answer("Menga tug'ilgan sanangizni <b>30.09.2001</b> ushbu formatda yuboring.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
