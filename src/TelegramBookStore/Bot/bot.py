"""This module contains the Bot assembly"""

import config


from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, LabeledPrice, ReplyKeyboardRemove
from Data import bookData
from Keyboards import keyboards
from Messages import messages
from aiogram.filters import CommandStart

telegramToken = config.TELEGRAM_TOKEN


bot = Bot(token=telegramToken)

dispatcher = Dispatcher(bot=bot)


testPrice = [LabeledPrice(label="Купить", amount=19 * 100)]


@dispatcher.message(CommandStart())
async def command_start(message: Message):
    """Responds to the /start command inside the chat, and greets the user with more options"""
    await message.answer(text=messages.welcome_user(), reply_markup=keyboards.startMenu)


@dispatcher.callback_query(F.data == "books")
async def book_catalogue(callback: CallbackQuery):
    """Displays the book catalogue"""
    await callback.answer("")
    await callback.message.answer(text=messages.book_catalgoue(),
                                  reply_markup=keyboards.bookCatalogueMenu
                                  )


@dispatcher.callback_query(F.data == "back")
async def back_to_menu(callback: CallbackQuery):
    """Returns user to main menu"""
    await callback.answer("")
    await callback.message.answer(
        text=messages.welcome_user(), reply_markup=keyboards.bookCatalogueMenu
    )


@dispatcher.callback_query(F.data == "info-peter")
async def callback_peter(callback: CallbackQuery):
    """When user select Peter's book"""
    await callback.answer("")
    print(callback.data)
    await callback.message.answer(
        text=f"Название книги: {bookData.baunovBookData.getTitle()}"
    )
    await callback.message.answer_photo(photo=bookData.baunovBookData.getImageUrl())
    await callback.message.answer(
        text=f"Описание:{bookData.baunovBookData.getDescription()} \n",
    )
    await callback.message.answer(
        text=f"Цена: {bookData.baunovBookData.getPrice()}.00€",
        reply_markup=keyboards.peterBookMenu,
    )


@dispatcher.callback_query(F.data == "buy-peter")
async def callback_buy(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        text="Вы выбрали: Петр Андрушевич, «EL RUSO. Свой в Испании».\nХотите добавить персональную подпись автора? (максимум 50 символов)",
        reply_markup=keyboards.peterCustomizationMenu,
    )


@dispatcher.callback_query(F.data == "buy--peter--autograph")
async def callback_buyPeterAutograph(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        text="Напишите, пожалуйста, текст для автографа, будут написаны только первые 50 символов."
    )
    await callback.message.answer("Text goes here:", reply_markup=ReplyKeyboardRemove())


@dispatcher.callback_query(F.data == "buy--peter--no-autograph")
async def callback_buyPeterNoAutograph(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        text="Продолжить оформление заказа?",
        reply_markup=keyboards.peterCustomizationMenuStep2NoAutograph,
    )


@dispatcher.callback_query(F.data == "buy--peter--no-autograph--no-coupon")
async def callback_buyPeterNoAutograph(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer_invoice(
        title=bookData.baunovBookData.getTitle(),
        description=bookData.baunovBookData.getDescription(),
        photo_url=bookData.rusoGuruBook.getImageUrl(),
        provider_token=config.PAYMENTS_TOKEN,
        payload="test",
        currency="eur",
        prices=testPrice,
    )


@dispatcher.message()
async def echo(message: Message):
    await message.answer(
        text=messages.unknown_command_message(), reply_markup=keyboards.bookCatalogueMenu
    )


async def main():
    await dispatcher.start_polling(bot)
