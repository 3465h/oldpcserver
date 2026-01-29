import asyncio
import psutil
import platform
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Вставь сюда свой токен от BotFather
TOKEN = "ТВОЙ_ТОКЕН_ЗДЕСЬ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /specs — выдает характеристики твоего старичка
@dp.message(Command("specs"))
async def get_specs(message: types.Message):
    # Считаем проц
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    # Считаем память
    ram = psutil.virtual_memory()
    ram_total = round(ram.total / (1024**3), 2)
    ram_used = round(ram.used / (1024**3), 2)
    
    # Инфо о системе
    uname = platform.uname()
    
    response = (
        f"🖥 **Характеристики сервера:**\n\n"
        f"🔹 **ОС:** {uname.system} {uname.release} (Alpine)\n"
        f"🔹 **Процессор:** {uname.processor} ({cpu_count} ядра)\n"
        f"🔹 **Загрузка CPU:** {cpu_usage}%\n"
        f"🔹 **Оперативка:** {ram_used}ГБ / {ram_total}ГБ\n"
        f"🔹 **Uptime:** {round(psutil.boot_time() / 3600, 1)} ч."
    )
    await message.answer(response, parse_mode="Markdown")

# Эхо-режим: отвечает тем же сообщением
@dp.message()
async def echo_all(message: types.Message):
    # Если это текст — шлем текст, если картинка — картинку
    try:
        await message.copy_to(chat_id=message.chat.id)
    except Exception as e:
        await message.answer("Не могу это повторить :(")

async def main():
    print("Бот запущен на твоем Dual Core!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
