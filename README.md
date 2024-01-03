
# Telegram Bookstore Bot
### By Alex Andrushevich

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=QuantGeekDev_telegram-store-bot&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=QuantGeekDev_telegram-store-bot)

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=QuantGeekDev_telegram-store-bot&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=QuantGeekDev_telegram-store-bot)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=QuantGeekDev_telegram-store-bot&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=QuantGeekDev_telegram-store-bot)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=QuantGeekDev_telegram-store-bot&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=QuantGeekDev_telegram-store-bot)

Basic Telegram bot that allows to sell hardcoded books
This is for two books, without plans for adding further books down the line - hence the choice to hardcode the book data

Future implementations will fetch book data from an API, allowing a manager to add books to the book api and edit the books on display

To run, use:
```python src/TelegramBookStore/main.py```

Make sure to create a config.py file in your src/TelegramBookStore directory and add your telegram bot token:

`TELEGRAM_TOKEN = <yourTokenGoesHere>`

Developed in Python 3.11.5
