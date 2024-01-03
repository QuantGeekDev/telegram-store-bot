
# Telegram Bookstore Bot
### By Alex Andrushevich

Basic Telegram bot that allows to sell hardcoded books
This is for two books, without plans for adding further books down the line - hence the choice to hardcode the book data

Future implementations will fetch book data from an API, allowing a manager to add books to the book api and edit the books on display

To run, use:
```python src/TelegramBookStore/main.py```

Make sure to create a config.py file in your src/TelegramBookStore directory and add your telegram bot token:

`TELEGRAM_TOKEN = <yourTokenGoesHere>`

Developed in Python 3.11.5
