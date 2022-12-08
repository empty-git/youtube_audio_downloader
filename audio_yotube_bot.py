import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pytube import YouTube

TOKEN = "5923567887:AAGzpP7iQvezL-G9-GBSelG7rDiZ1Gp8b6Y"


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Вітаю, надішли мені список посилань на ютуб відео або ж одне і я завантажу його аудіо для тебе ;)\nРозробник @redcore")





@dp.message_handler()
async def echo_message(msg: types.Message):
    if "https" in msg.text:
        links = msg.text.split("\n")
        await bot.send_message(chat_id=msg.chat.id,text="Посилання отримано, починаю скачування....")
        for link in links:
            path_audio = YouTube(link).streams.filter(only_audio=True).first().download()
            await bot.send_audio(chat_id=msg.chat.id, audio=open(path_audio,mode="rb"))
            os.remove(path_audio)
    #await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
