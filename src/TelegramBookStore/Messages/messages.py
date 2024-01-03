'''This module contains messages used by the bookstore'''


def welcome_user() -> str:
    ''' Welcomes the User'''
    welcome_message = "👋🏼 Добро пожаловать в Телеграм-магазин  «Маньяна и Авось» \
        \nЧто бы вы хотели сделать? \n"
    return f"{welcome_message}"


def book_catalgoue() -> str:
    ''' Introduces the book catalogue'''
    book_catalgoue_message = "📚 Вот наши доступные книги:"
    return f"{book_catalgoue_message}"


def get_user_id(message) -> str:
    '''Get the user's telegram ID'''
    text: str = "Your ID is: "
    return f"{text}{message.from_user.id}"


def get_username(message) -> str:
    '''Get the users username'''
    text: str = "Your username is: "
    return f"{text}{message.from_user.username}"


def get_user_first_name(message) -> str:
    '''Get the user's first name'''
    text: str = "Your first name is: "
    first_name = message.from_user.first_name
    if first_name:
        return f"{text}{first_name}"
    return ""


def get_user_last_name(message) -> str:
    '''Get the user's last name'''
    text: str = "Your last name is: "
    last_name = message.from_user.last_name
    if last_name:
        return f"{text}{last_name}"
    return ""


def unknown_command_message() -> str:
    '''Sends an error message if the command is not defined'''
    text: str = "Я не знаю этой команды, извините 😔. Пожалуйста, попробуйте еще раз."
    return text
