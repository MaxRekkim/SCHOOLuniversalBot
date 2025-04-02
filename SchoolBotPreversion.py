from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='7976563143:AAHQgetnysWE2T8WaY_0KLpH8gFiJEmxqX0')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Восстановить карту")
    keyboard.add(button_1)
    button_2 = "Администрация"
    keyboard.add(button_2)
    button_3 = "Расписание звонков"
    keyboard.add(button_3)
    button_4 = "Расписание уроков"
    keyboard.add(button_4)
    button_5 = "График работы мед. кабинета"
    keyboard.add(button_5)
    button_6 = "Доп. образование"
    keyboard.add(button_6)
    button_7 = "Новости школы"
    keyboard.add(button_7)
    button_8 = "Меню школьной столовой"
    keyboard.add(button_8)
    button_9 = "Служба сопровождения"
    keyboard.add(button_9)
    button_10 = "Тех.поддержка"
    keyboard.add(button_10)
    await message.answer("Чем вам помочь?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Восстановить карту')
async def with_puree(message: types.Message):
    await message.reply(
        'В кабинете №238 можно восстановить карту по средам и пятницам с 13:00 до 16:00. Для восстановления на счёте карты нужно иметь 100 рублей. Не теряй и не ломай больше карту, хорошего дня :) ')


@dp.message_handler(lambda message: message.text == "Тех.поддержка")
async def cmd_inline_url(message: types.Message):
    buttons = [types.InlineKeyboardButton(text="Нажми на меня", url="https://t.me/supserv_bot")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Вознили вопросы?👇🏻👇🏻👇🏻", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Администрация')
async def with_puree(message: types.Message):
    await message.reply(
        'Лудкова Олеся Анатольенва(директор школы) - приём по четвергам с 14:00 до 17:00.\n'
        'Бекяшева Диана Робертовна(зам. директора по УВР Ст. школы) - приём по вторникам с 14:00 до 17:00.\n'
        'Матвеева Людмила Владиславовна(Зам. директора по УВР Мл. школы) - приём по вторникам с 14:00 до 17:00.\n'
        'Уважаемые родители, приём осуществляется по предварительной записи по телефону: +7 (812) 247-44-52')


@dp.message_handler(lambda message: message.text == 'Расписание звонков')
async def with_puree(message: types.Message):
    await message.reply('1 урок:8:30-9:15\n'
                        '2 урок:9:35-10:20\n'
                        '3 урок:10:40-11:25\n'
                        '4 урок:11:45-12:30\n'
                        '5 урок:12:50-13:35\n'
                        '6 урок:13:55-14:40\n'
                        '7 урок:14:50-15:35\n'
                        '8 урок:15:45-16:30\n'
                        '9 урок:16:40-17:25')


@dp.message_handler(lambda message: message.text == "Расписание уроков")
async def cmd_inline_url(message: types.Message):
    buttons = [types.InlineKeyboardButton(
        text="Ссылка",
        url="https://drive.google.com/drive/folders/1KRfvv-tOp7Kj_s1LLewOmw91jgn7wGD-?usp=sharing")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Расписание можно посмотреть тут", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Новости школы")
async def cmd_inline_url(message: types.Message):
    buttons = [types.InlineKeyboardButton(text="Группа Вконтакте", url="https://vk.com/sch100spb")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Новости можно помотреть тут👇🏻👇🏻👇🏻", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'График работы мед. кабинета')
async def with_puree(message: types.Message):
    await message.reply('Мед. кабинет работает с пн по пт с 9:00 до 17:00')


@dp.message_handler(lambda message: message.text == "Доп. образование")
async def cmd_inline_url(message: types.Message):
    buttons = [types.InlineKeyboardButton(
        text="Расписание занятий",
        url="https://drive.google.com/drive/folders/1doFatEHoJuurHFqnpSzKc4WmUKwy55pC?usp=sharing"),
        types.InlineKeyboardButton(
            text="Правила приема, перевода и отчисления обучающихся ОДОД",
            url="http://school100spb.ru/wp-content/uploads/2021/03/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC-%D0%BE%D1%82%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-%D0%9E%D0%94%D0%9E%D0%94-1.pdf"),
        types.InlineKeyboardButton(
            text="Положение ОДОД",
            url="http://school100spb.ru/wp-content/uploads/2021/03/%D0%9F%D0%9E%D0%9B%D0%9E%D0%96%D0%95%D0%9D%D0%98%D0%95-%D0%9E%D0%94%D0%9E%D0%94.pdf"),
        types.InlineKeyboardButton(
            text="Основный сведения",
            url="http://school100spb.ru/podrazdeleniya/odod/informaciya/"),
        types.InlineKeyboardButton(
            text="Платные образовательные услуги",
            url="https://drive.google.com/drive/folders/1PSE-uaekWO426cjV0HqsH-VonMhCScIt?usp=sharing")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Актуальная информация ОДОД👇🏻👇🏻👇🏻", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Меню школьной столовой")
async def cmd_inline_url(message: types.Message):
    buttons = [types.InlineKeyboardButton(
        text="Завтраки, обеды",
        url="https://drive.google.com/drive/folders/17HW_TzDHduO6-8vp3juaeMXNSJrvo6M3?usp=sharing")]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Актуальное меню школы👇🏻👇🏻👇🏻", reply_markup=keyboard)


# @dp.message_handler(lambda message: message.text == "Служба сопровождения")
# async def cmd_inline_url(message: types.Message):
#     buttons = [types.InlineKeyboardButton(text="Контакт", url="")]
#     keyboard = types.InlineKeyboardMarkup(row_width=1)
#     keyboard.add(*buttons)
#     await message.answer("                                                                          К ней можно обратиться с пн по пт с 9:15 до 17:00.                                                                                                       Записаться можно тут 👇🏻👇🏻👇🏻", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
