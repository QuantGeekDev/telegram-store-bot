import config as config


from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, LabeledPrice, ReplyKeyboardRemove
from Data import bookData
from Keyboards import keyboards
from Messages import messages

telegramToken = config.TELEGRAM_TOKEN


bot = Bot(token=telegramToken)

dispatcher = Dispatcher(bot=bot)


testPrice = [LabeledPrice(label="Купить", amount=19*100)]



@dispatcher.message(F.text == "/start")
async def command_start(message: Message):
    await message.answer(text=messages.welcomeUser(), reply_markup=keyboards.mainMenu)

@dispatcher.callback_query(F.data == "back")
async def backToMenu(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(text=messages.welcomeUser(), reply_markup=keyboards.mainMenu)

@dispatcher.callback_query(F.data == "info-peter")
async def callback_Peter(callback: CallbackQuery):
    await callback.answer("")
    print(callback.data)
    await callback.message.answer(text=f"Название книги: {bookData.rusoGuruBookData.getTitle()}")
    await callback.message.answer_photo(photo=bookData.rusoGuruBookData.getImageUrl())
    await callback.message.answer(text=f"Описание:{bookData.rusoGuruBookData.getDescription()} \n", )
    await callback.message.answer(text=f"Цена: {bookData.rusoGuruBookData.getPrice()}.00€", reply_markup=keyboards.peterBookMenu)

@dispatcher.callback_query(F.data == "buy-peter")
async def callback_buy(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(text="Вы выбрали: Петр Андрушевич, «EL RUSO. Свой в Испании».\nХотите добавить персональную подпись автора? (максимум 50 символов)", reply_markup=keyboards.peterCustomizationMenu)

@dispatcher.callback_query(F.data == "buy--peter--autograph")
async def callback_buyPeterAutograph(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(text="Напишите, пожалуйста, текст для автографа, будут написаны только первые 50 символов.")
    await callback.message.answer("Text goes here:", reply_markup=ReplyKeyboardRemove())



@dispatcher.callback_query(F.data == "buy--peter--no-autograph")
async def callback_buyPeterNoAutograph(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(text="Продолжить оформление заказа?", reply_markup=keyboards.peterCustomizationMenuStep2NoAutograph)


@dispatcher.callback_query(F.data == "buy--peter--no-autograph--no-coupon")
async def callback_buyPeterNoAutograph(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer_invoice(title=bookData.rusoGuruBookData.getTitle(), description=bookData.rusoGuruBookData.getDescription(), photo_url=rusoGuruBook.getImageUrl(), provider_token=config.PAYMENTS_TOKEN ,payload="test", currency="eur", prices=testPrice)



@dispatcher.message()
async def echo(message: Message):
    await message.answer(text=messages.unknownCommandMessage(), reply_markup=keyboards.mainMenu)
async def main():
    await dispatcher.start_polling(bot)


