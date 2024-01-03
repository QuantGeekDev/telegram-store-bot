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
    """Returns user to book menu"""
    await callback.answer("")
    await callback.message.answer(
        text=messages.welcome_user(), reply_markup=keyboards.bookCatalogueMenu
    )


@dispatcher.callback_query(F.data == "back-to-main")
async def back_to_main_menu(callback: CallbackQuery):
    """Returns user to main menu"""
    await callback.answer("")
    await callback.message.answer(
        text=messages.welcome_user(), reply_markup=keyboards.startMenu)


@dispatcher.callback_query(F.data == "book-peter")
async def callback_peter(callback: CallbackQuery):
    """When user select Peter's book"""
    await callback.answer("")
    print(callback.data)
    await callback.message.answer(
        text=f"Название книги: {bookData.rusoGuruBookData.getTitle()}"
    )
    await callback.message.answer_photo(photo=bookData.rusoGuruBookData.getImageUrl())
    await callback.message.answer(
        text=f"Описание:{bookData.rusoGuruBookData.getDescription()} \n",
    )
    await callback.message.answer(
        text=f"Цена: {bookData.rusoGuruBookData.getPrice()}.00€",
        reply_markup=keyboards.peterBookMenu,
    )


@dispatcher.callback_query(F.data == "buy-peter")
async def callback_buy(callback: CallbackQuery):
    ''' When user selects Peter's book, offers autograph customization options'''
    await callback.answer("")
    await callback.message.answer(
        text="Вы выбрали: Петр Андрушевич, «EL RUSO. Свой в Испании».\nХотите добавить персональную подпись автора? (максимум 50 символов)",
        reply_markup=keyboards.peterCustomizationMenu,
    )


@dispatcher.callback_query(F.data == "buy--peter--autograph")
async def callback_buy_peter_autograph(callback: CallbackQuery):
    ''' When user selects buy Peter's book with autograph'''
    await callback.answer("")
    await callback.message.answer(
        text="Вы выбрали книгу с автографом\n",
        reply_markup=keyboards.peterBookBuyAutographMenu
    )


@dispatcher.callback_query(F.data == "buy--peter--no-autograph")
async def callback_buy_peter_no_autograph_no_coupon(callback: CallbackQuery):
    ''' When user selects no autograph option, redirects to stripe purchase page'''
    await callback.answer("")
    await callback.message.answer(
        text="Вы выбрали книгу без автографа\n",
        reply_markup=keyboards.peterBookBuyNoAutographMenu
    )


@dispatcher.message()
async def echo(message: Message):
    ''' If command is not registered'''
    await message.answer(
        text=messages.unknown_command_message(), reply_markup=keyboards.bookCatalogueMenu
    )


async def main():
    ''' Main launch command with long polling option'''
    await dispatcher.start_polling(bot)
