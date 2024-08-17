from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) 
        await message.answer(text=f"Assalomu alaykum {full_name} ! , Bu bot orqali siz rasmlaringizning orqa fonini osonlik bilan o'zgartirishingiz mumkin 🖼 ")
    except:
        await message.answer(text="Botdan foydalanish uchun rasm yuboring 🖼")

