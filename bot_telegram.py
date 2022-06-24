from asyncore import dispatcher
from cgitb import text
from pickle import TRUE
from xml.dom.minidom import Document
from aiogram.types import input_file
from email import message
from msvcrt import kbhit
from aiogram.dispatcher.filters import Text
from random import randint
from tkinter import Text
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, callback_query
from aiogram.types import ContentTypes, Message
from aiogram.types import file
import asyncio
from aiogram.types import InputFile
from aiogram.types.file import File
from setuptools import Command

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

#Консольная информация
async def on_startup(_):
    print('\n\nБот вышел в онлайн!\n\nОшибок не обнаружено\n\nРазработано: lamarel-web.ru')


# 0/3    /Start --- начало 
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("1", callback_data="but1")
    download = InlineKeyboardButton("2", callback_data="download")
    but3 = InlineKeyboardButton("3", callback_data="but3")
    markup.add(but1, download, but3)
    await bot.send_message(message.chat.id, "На связи команда Karolina style.\n\nБлагодарим Вас за выбор нашего бренда.Мы хотим тебя отблагодарить.\n\nВыбери подарок, который заберёшь и отправь соответствующую цифру:\n\n1.Бонус 100 RUB за отзыв о товаре 🌟 🌟🌟🌟🌟\n\n2. Летний Шопинг гид по стилю\n\n3. У меня возник вопрос/проблема (доставка, служба качества, возврат, брак)", reply_markup=markup)




# 1/3 Бонус 100 RUB за отзыв о товаре
@dp.callback_query_handler(lambda c: c.data == "but1")
async def button_reaction(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    but4 = InlineKeyboardButton("1", callback_data="but4")
    but5 = InlineKeyboardButton("2", callback_data="but5")
    but6 = InlineKeyboardButton("3", callback_data="but6")
    markup.add(but4, but5, but6)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Для начала, хотим сказать спасибо за выбор бренда Karolina style. Это нас очень вдохновляет.\n\nА еще, для нас важно твое впечатление о нашей продукции. Поэтому мы дарим 100 RUB за отзыв о каждом заказанном товаре Karolina style, оставленный на Wildberries.\n\nКлассно, правда?\n\nЕсли ты вдруг уже оставил(-а) свой отзыв, то наш денежный\nбонус все равно к тебе прилетит😉\n\n1️⃣Пришли цифру 1, если уже оставил(-а) отзыв\n2️⃣Пришли цифру 2, чтобы узнать условия получения бонуса\n3️⃣Пришли цифру 3, если возник вопрос / проблема. ❗️Чтобы вернуться в начало, напиши в чат: /start", reply_markup=markup)

# 2/3 Скачать пдф
@dp.callback_query_handler(lambda c: c.data == "download")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_document(call.message.chat.id, document=open('leto.pdf', 'rb'))

@dp.callback_query_handler(lambda c: c.data == "but3")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id , "3️⃣ Опиши проблему, которая у тебя возникла. Менеджер Karolina style тебе поможет и ответит на все твои вопросы. Напишите мне: @ksenia_el")



#@dp.message_handler(lambda c: c.data == "download", commands="download")
#async def cmd_start(message: types.Message):
#await bot.send_document(message.chat.id, document=open('leto.pdf', 'rb'))

# 2/3 Летний Шопинг гид по стилю pdf
#@dp.message_handler(commands="download")
#async def cmd_random(message: types.Message):
       # await bot.send_document(message.chat.id, document=open('leto.pdf', 'rb'))




    
# Пришли цифру 1, если уже оставил(-а) отзыв
@dp.callback_query_handler(lambda c: c.data == "but4")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    markup = InlineKeyboardMarkup()
    #but6 = InlineKeyboardButton("3", callback_data="but6")
    photo = open('bonus.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo, caption="1️⃣ Супер, спасибо тебе!😘\n\nВ таком случае, ждем скриншот твоего отзыва, и 100 RUB очень скоро будут у тебя.\n\nВ примере ниже мы оставили наглядную инструкцию, как сделать скриншот.\n\nПосле его отправки, пожалуйста, дождись ответа наших менеджеров.\n\nВ Личном кабинете WB все оставленные отзывы можно найти в разделе ➡️ Профиль ➡️ Отзывы и вопросы. ❗️Чтобы вернуться в начало, напиши в чат: /start", reply_markup=markup)

# Пришли цифру 2 что бы узнать условия
@dp.callback_query_handler(lambda c: c.data == "but5")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    photo = open('bonus.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo, caption="Для того, чтобы получить свой денежный бонус, тебе нужно оставить отзыв. Расскажи, что тебе понравилось в Karolina style: продукт, упаковка, сервис, доставка. Прикрепи фото (это по желанию, но нам будет приятно).\n\n ❗️Обрати внимание на то, чтобы наш секретный вкладыш не попал в кадр. О нем знаем только мы с тобой😉\n\nСледуй по пунктам, и у тебя все получится 🤍:\n\n1️⃣ Зайди в Личный кабинет\n2️⃣ Найди раздел “Покупки”\n3️⃣ Выбери товар бренда Karolina style, который ты приобрел(-а).\n4️⃣ Кликни на “Отзыв”, далее – “Оставить отзыв”\n5️⃣ Напиши, чем тебе понравился наш бренд\n6️⃣ Кликни “Опубликовать отзыв”\n7️⃣ Сделай скриншот готового отзыва и прикрепи в наш чат-бот\n❗️Чтобы вернуться в начало, напиши в чат: /start")

#  Возникли проблемы нажми 3
@dp.callback_query_handler(lambda c: c.data == "but6")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id , "3️⃣ Опиши проблему, которая у тебя возникла. Менеджер Karolina style тебе поможет и ответит на все твои вопросы. Напишите мне: @ksenia_el")



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


@dp.message_handler(lambda message: message.text == "1")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="1", callback_data="random_value1"))
    keyboard.add(types.InlineKeyboardButton(text="2", callback_data="random_value2"))
    keyboard.add(types.InlineKeyboardButton(text="3", callback_data="random_value3"))
    await message.answer("Для начала, хотим сказать спасибо за выбор бренда Karolina style. Это нас очень вдохновляет.\n\nА еще, для нас важно твое впечатление о нашей продукции. Поэтому мы дарим 100 RUB за отзыв о каждом заказанном товаре Karolina style, оставленный на Wildberries.\n\nКлассно, правда?\n\nЕсли ты вдруг уже оставил(-а) свой отзыв, то наш денежный\nбонус все равно к тебе прилетит😉\n\n1️⃣Пришли цифру 1, если уже оставил(-а) отзыв\n2️⃣Пришли цифру 2, чтобы узнать условия получения бонуса\n3️⃣Пришли цифру 3, если возник вопрос / проблема", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "2")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="вернуться назад", callback_data="testing"))
    await message.answer("В данный момент раздел находиться в стадии разработки, приносим свои извенения", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "3")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    mar2 = types.KeyboardButton("Назад в меню")
    keyboard.add(types.InlineKeyboardButton(text="Вернуться", callback_data="/testing"))
    await message.answer("3️⃣ Опиши проблему, которая у тебя возникла. Менеджер Karolina style тебе поможет и ответит на все твои вопросы.", reply_markup=keyboard)


#@dp.message_handler(commands="random")
#async def cmd_random(message: types.Message):
    #keyboard = types.InlineKeyboardMarkup()
    #keyboard.add(types.InlineKeyboardButton(text="1.Бонус 100 RUB за отзыв о товаре 🌟🌟🌟🌟🌟", callback_data="random_value1"))
    #keyboard.add(types.InlineKeyboardButton(text="3. У меня возник вопрос/проблема (доставка, служба качества, возврат, брак)", callback_data="random_value3"))
    #await message.answer("На связи команда Karolina style.\n\nБлагодарим Вас за выбор нашего бренда.Мы хотим тебя отблагодарить.\n\nВыбери подарок, который заберёшь и отправь соответствующую цифру:\n\n1.Бонус 100 RUB за отзыв о товаре 🌟 🌟🌟🌟🌟\n\n2. Летний Шопинг гид по стилю\n\n3. У меня возник вопрос/проблема (доставка, служба качества, возврат, брак)", reply_markup=keyboard)

#Менюшки

@dp.callback_query_handler(text="random_value1")
async def send_random_value(call: types.CallbackQuery):
  await call.message.answer('1️⃣ Супер, спасибо тебе!😘\n\nВ таком случае, ждем скриншот твоего отзыва, и 100 RUB очень скоро будут у тебя.\n\nВ примере ниже мы оставили наглядную инструкцию, как сделать скриншот.\n\nПосле его отправки, пожалуйста, дождись ответа наших менеджеров.\n\nВ Личном кабинете WB все оставленные отзывы можно найти в разделе "Профиль” ➡️ “Отзывы и вопросы ".')

@dp.callback_query_handler(text="random_value2")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer('Для того, чтобы получить свой денежный бонус, тебе нужно оставить отзыв. Расскажи, что тебе понравилось в Karolina style: продукт, упаковка, сервис, доставка. Прикрепи фото (это по желанию, но нам будет приятно).\n\n ❗️Обрати внимание на то, чтобы наш секретный вкладыш не попал в кадр. О нем знаем только мы с тобой😉\n\nСледуй по пунктам, и у тебя все получится 🤍:\n\n1️⃣ Зайди в Личный кабинет\n2️⃣ Найди раздел “Покупки”\n3️⃣ Выбери товар бренда Karolina style, который ты приобрел(-а).\n4️⃣ Кликни на “Отзыв”, далее – “Оставить отзыв”\n5️⃣ Напиши, чем тебе понравился наш бренд\n6️⃣ Кликни “Опубликовать отзыв”\n7️⃣ Сделай скриншот готового отзыва и прикрепи в наш чат-бот\n❗️Чтобы вернуться в начало, отправь')
    #await call.message.answer_photo(photo="")
    #photo = open('nft.jpg', 'rb')
    #await bot.send_photo(chat_id=message.chat.id, photo=photo)
    #await bot.send_message("Фотография успешно загружена!")


@dp.callback_query_handler(text="random_value3")
async def send_random_value(call: types.CallbackQuery):
  await call.message.answer('3️⃣ Опиши проблему, которая у тебя возникла. Менеджер Karolina style тебе поможет и ответит на все твои вопросы.\n\n❗️Чтобы вернуться в начало, отправь')



# end test

 #@dp.callback_query_handler(text='button1')
#async def menu_index(call: types.CallbackQuery):
    #await call.message.answer_photo(photo="AgACAgIAAxkBAAIyU2E2IvI_uHqhjorlNFAmvlxxsbWeAAIPtTEbL52xScailMfWbabxAQADAgADeAADIAQ")
# Общая часть
#@dp.message_handler()
#async def echo_send(message : types.Message):
    #if message.text == '/start':
    #await message.answer('На связи команда Karolina style.\n\nБлагодарим Вас за выбор нашего бренда.Мы хотим тебя отблагодарить.\n\nВыбери подарок, который заберёшь и отправь соответствующую цифру:\n\n1.Бонус 100 RUB за отзыв о товаре 🌟 🌟🌟🌟🌟\n\n2. Летний Шопинг гид по стилю\n\n3. У меня возник вопрос/проблема (доставка, служба качества, возврат, брак)')
        
   # await message.answer(message.text)
   # await message.reply(message.text)
   # await bot.send_message(message.from_user.id, message.text)




