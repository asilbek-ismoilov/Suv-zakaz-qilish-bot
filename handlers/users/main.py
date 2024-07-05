from loader import dp, bot, ADMINS, CHANNELS
import asyncio
from aiogram import F
from states.suv_stt import Zakazqilish
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboard_buttons.default.location import kv
from keyboard_buttons.default.water_button import num_water
from keyboard_buttons.inline import inline_val


@dp.message(F.text=="Zakas qilish 🛎")
async def zakaz_button(message:Message, state:FSMContext):
    text ="Suv buyurtma qilmoqchi bo'lsangiz ma'lumotlarni kiriting ❗️ \n\n<b>Ismingizni kiriting</b> ✍"
    await message.answer(text)
    await state.set_state(Zakazqilish.name)
# name
@dp.message(F.text, Zakazqilish.name)
async def name(message:Message, state:FSMContext):
    name = message.text
    await state.update_data(name = name)
    await message.answer("Familiyani kiriting ❗️")
    await state.set_state(Zakazqilish.surname)

@dp.message(Zakazqilish.name)
async def name_del(message:Message, state:FSMContext):
    await message.answer(text= "Ismni to'g'ri kiriting ❗️")
    await message.delete()
#surname
@dp.message(F.text, Zakazqilish.surname)
async def surname(message:Message, state:FSMContext):
    surname = message.text
    await state.update_data(surname = surname)
    await message.answer("☎️ Telefon raqamingizni kiriting ❗️")
    await state.set_state(Zakazqilish.tel)

@dp.message(Zakazqilish.surname)
async def surname_del(message:Message, state:FSMContext):
    await message.answer(text= "Familiyani to'g'ri kiriting ❗️")
    await message.delete()
# phone
@dp.message(F.text.regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"), Zakazqilish.tel)
async def phone_number(message:Message, state:FSMContext):
    phone = message.text
    await state.update_data(phone = phone)
    await message.answer("📍 Joylashuvni (location) yuboring ❗️", reply_markup=kv)
    await state.set_state(Zakazqilish.location)

@dp.message(Zakazqilish.tel)
async def phone_number_del(message:Message):
    await message.answer(text= "Telefon raqamni to'g'ri kiriting ❗️")
    await message.delete()
# Location
@dp.message(F.location, Zakazqilish.location)
async def get_location(message: Message, state:FSMContext):
    lat = message.location.latitude
    long = message.location.longitude
    await state.update_data(lat = lat)
    await state.update_data(long = long)
    await message.answer('Suv sonini kiriting ❗️', reply_markup=num_water)
    await state.set_state(Zakazqilish.sav_son)

@dp.message(Zakazqilish.location)
async def location_del(message:Message):
    await message.answer(text= "Joylashuvni to'g'ri kiriting ❗️")
    await message.delete()


@dp.message(F.text, Zakazqilish.sav_son)
async def number_water(message: Message, state:FSMContext):
    data = await state.get_data()

    name = data.get("name")
    surname = data.get("surname")
    phone = data.get("phone")
    lat = data.get("lat")
    long = data.get("long")
    water = message.text

    text = f"⚠️ Yangi buyurtma ❗️ \n Ism-Familiya: {name} {surname} \nTel: {phone} \nSuv soni: {water}"

    f_text = f"Ism-Familiya: {name} {surname} \nTel: {phone} \nSuv soni: {water} \n\nMa'lumot adminga yuborildi ✅ \nKun davomida sizga suv yetkazib berinadi ✅"

    sent_message = await message.answer(f_text, reply_markup=inline_val.confirmation)
    await bot.send_location(chat_id=CHANNELS[0], latitude=lat, longitude=long)
    await bot.send_message(chat_id=CHANNELS[0], text=text, reply_markup=inline_val.deliver)
    await state.clear()

    await asyncio.sleep(3600)
    await sent_message.edit_reply_markup(reply_markup=None)

    
@dp.message(Zakazqilish.sav_son)
async def number_water_del(message:Message, state:FSMContext):
    await message.answer(text= "To'g'ri qiymat kiriting !")
    await message.delete()

@dp.callback_query(F.data == "edit")
async def confirmation(callback:CallbackQuery):
    await callback.message.edit_text("Ma'lumotlaringizni yangilang:")

@dp.callback_query(F.data == "deliver")
async def confirmation(callback:CallbackQuery):
    await callback.message.delete()
    text = "Buyurtma yetkazib berinldi ✅"
    await callback.message.answer(text)
    
