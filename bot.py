import config
import logging
import asyncio

from aiogram import Bot, Dispatcher, types, Router

telegramToken = config.TELEGRAM_TOKEN

bookPrice = types.LabeledPrice(label="Comprar Ahora", amount=15*100)

bot = Bot(token=telegramToken)
dispatcher = Dispatcher(bot=bot)


async def main():
    await dispatcher.start_polling(bot)


asyncio.run(main())
