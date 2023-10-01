import config
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import messages
from books import ElRusoBook

telegramToken = config.TELEGRAM_TOKEN


bot = Bot(token=telegramToken)

dispatcher = Dispatcher(bot=bot)

book = ElRusoBook(id=1,
                  title="El Ruso Guru",
                  description="Test Description",
                  price=10,
                  pages=250,
                  imageUrl="https://i.imgur.com/rJtag7i.jpg")


@dispatcher.message(F.text == "/start")
async def command_start(message: Message):
    await message.reply(text=messages.welcomeUser(message))


@dispatcher.message(F.text == "/my_id")
async def command_myId(message: Message):
    await message.reply(text=messages.getUserId(message))
    await message.reply(text=messages.getUsername(message))
    await message.reply(text=messages.getUserFirstName(message))
    await message.reply(text=messages.getUserLastName(message))


@dispatcher.message(F.text == "/book_info")
async def command_bookInfo(message: Message):
    await message.answer(text=book.getTitle())
    await message.answer_photo(photo=book.getImageUrl(), caption="Обложка 'El Ruso Guro'")
    await message.answer(text=book.getDescription())
    await message.answer(text=book.getPrice())



@dispatcher.message()
async def echo(message: Message):
    await message.answer(text=messages.getUnknownCommandMessage())
async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())

    except:
        print("Exit")
