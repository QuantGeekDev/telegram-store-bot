import config
import logging
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

telegramToken = config.TELEGRAM_TOKEN


bot = Bot(token=telegramToken)
dispatcher = Dispatcher(bot=bot)


@dispatcher.message(F.text == "/start")
async def command_start(message: Message):
    await message.answer(text="Welcome to the test bot!")


async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
