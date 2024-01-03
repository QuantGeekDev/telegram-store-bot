import asyncio

from Bot.bot import main as start_bot

async def main():
    await start_bot()

if __name__ == "__main__":
    try:
        print("\nAndrusoft 2023")
        print("Launching Telegram Bookstore Bot")
        asyncio.run(main())
    except Exception:
        print(f"Error launching Telegram Bookstore Bot: \n {Exception}")