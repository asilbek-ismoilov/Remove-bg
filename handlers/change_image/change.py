from aiogram import  F, types
from aiogram.types import Message, CallbackQuery
from keyboard_buttons.inlinebuttonss import colors_button
from loader import dp, bot, TOKEN
from removebg import remove_bg
from removebgpic import remove_bg_pic

@dp.message(lambda message: not message.photo)
async def photo_del(message: types.Message):
    await message.answer(text= "Faqat rasm yuboring ❗️")
    await message.delete()

@dp.message(F.photo)
async def photo(message:Message):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg(photos_url)
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)

# black
@dp.callback_query(F.data=="black")
async def black_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    print(file)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg(photos_url,"black")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()

# white
@dp.callback_query(F.data=="white")
async def white_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm =remove_bg(photos_url,"white")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()
# yellow
@dp.callback_query(F.data=="yellow")
async def yellow_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm =remove_bg(photos_url,"yellow")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()
# red
@dp.callback_query(F.data=="red")
async def red_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm =remove_bg(photos_url,"red")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()
# blue
@dp.callback_query(F.data=="blue")
async def blue_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm =remove_bg(photos_url,"blue")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()
# green
@dp.callback_query(F.data=="green")
async def green_handler(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm =remove_bg(photos_url,"green")
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    await callback.message.delete()


@dp.callback_query(F.data=="png")
async def png(callback: CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    
    rasm = remove_bg_pic(photos_url)
    text = "Rasmni orqa fonini qaysi ranga o'zgartirmoqchisiz tanlang !"

    if rasm:
        await callback.message.answer_document(document=types.input_file.BufferedInputFile(rasm, filename="no-bg.png"))
        await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button, caption=text)
    else:
        await callback.message.answer("Rasmning orqa fonini olib tashlashda xatolik yuz berdi.")
    await callback.message.delete()