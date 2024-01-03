def welcomeUser() -> str:
    welcomeMessage = "Добро пожаловать в Телеграм-магазин «Маньяна и Авось» \nЧто бы вы хотели сделать? \n🛒STORE"
    return f"{welcomeMessage}"


def getUserId(message) -> str:
    text: str = "Your ID is: "
    return f"{text}{message.from_user.id}"


def getUsername(message) -> str:
    text: str = "Your username is: "
    return f"{text}{message.from_user.username}"


def getUserFirstName(message) -> str:
    text: str = "Your first name is: "
    first_name = message.from_user.first_name
    if first_name:
        return f"{text}{first_name}"
    return ""


def getUserLastName(message) -> str:
    text: str = "Your last name is: "
    last_name = message.from_user.last_name
    if last_name:
        return f"{text}{last_name}"
    return ""


def unknownCommandMessage() -> str:
    text: str = "Я не знаю этой команды, извините 😔. Пожалуйста, попробуйте еще раз."
    return text
