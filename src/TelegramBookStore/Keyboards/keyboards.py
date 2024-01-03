''' This module contains custom keyboards used by the chatbot'''

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

startMenuKb = [
    [InlineKeyboardButton(
        text="🛒📚 Каталог книг", callback_data="books")],
    [InlineKeyboardButton(
        text="💬Связаться с нами", callback_data="contact")]
]

startMenu = InlineKeyboardMarkup(inline_keyboard=startMenuKb)

bookCatalgoueKb = [
    [InlineKeyboardButton(
        text="📖Петр Андрушевич, «EL RUSO. Свой в Испании»", callback_data="book-peter")],
    [InlineKeyboardButton(
        text="📖Александр Баунов, «Конец режима»", callback_data="book-alexandr")],
    [InlineKeyboardButton(text="🔙 Назад", callback_data="back")],
]

bookCatalogueMenu = InlineKeyboardMarkup(inline_keyboard=bookCatalgoueKb)

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
