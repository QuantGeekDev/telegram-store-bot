''' This module contains custom keyboards used by the chatbot'''

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

startMenuKb = [
    [InlineKeyboardButton(
        text="🛒📚 Каталог книг", callback_data="books")],
    [InlineKeyboardButton(
        text="💬Связаться с нами", callback_data="contact")]
]

startMenu = InlineKeyboardMarkup(inline_keyboard=startMenuKb)

mainMenuKb = [
    [InlineKeyboardButton(
        text="📖Петр Андрушевич, «EL RUSO. Свой в Испании»", callback_data="info-peter")],
    [InlineKeyboardButton(
        text="📖Александр Баунов, «Конец режима»", callback_data="alexandr")],
]

mainMenu = InlineKeyboardMarkup(inline_keyboard=mainMenuKb)

peterBookKb = [
    [InlineKeyboardButton(text="🛒 Купить", callback_data="buy-peter")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="back")],
]
peterBookMenu = InlineKeyboardMarkup(inline_keyboard=peterBookKb)


peterCustomizationKb = [
    [InlineKeyboardButton(text="персонализированный автограф автора (+6€)",
                          callback_data="buy--peter--autograph")],
    [InlineKeyboardButton(text="Продолжить без автографа",
                          callback_data="buy--peter--no-autograph")]
]

peterCustomizationMenu = InlineKeyboardMarkup(
    inline_keyboard=peterCustomizationKb)

peterCustomizationKbStep2NoAutograph = [
    [InlineKeyboardButton(text="Ввести купон",
                          callback_data="buy--peter--no-autograph--coupon")],
    [InlineKeyboardButton(text="Продолжить оформление заказа",
                          callback_data="buy--peter--no-autograph--no-coupon")]
]

peterCustomizationMenuStep2NoAutograph = InlineKeyboardMarkup(
    inline_keyboard=peterCustomizationKbStep2NoAutograph)
