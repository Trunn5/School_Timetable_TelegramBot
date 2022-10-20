from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    KeyboardButton, ReplyKeyboardMarkup

btnTimetableToday = KeyboardButton(text = "Расписание на сегодня")
btnTimetableTomorrow = KeyboardButton(text = "Расписание на завтра")
btnWhenCall = KeyboardButton(text = "Когда звонок?")
btnCallsTime = KeyboardButton(text = "Расписание звонков")
Menu = ReplyKeyboardMarkup(row_width=1)

Menu.add(btnTimetableToday, btnTimetableTomorrow, btnWhenCall, btnCallsTime)
