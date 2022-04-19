from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Добро пожаловать в бот группы KU22!\nКраткий перечень команд, которые вы можете использовать в нашем боте:\n/Расписание - показывает расписание занятий. \n /Список - высвечивает список группы. \n /Новости - последние новости')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс,напишите ему:https://t.me/KU22bot')
#@dp.message_handler(commands=['timetable'])
async def commands_timetable(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Выберите день: \n❤️/Понедельник❤️\n❤️/Вторник❤️\n❤️/Среда❤️\n❤️/Четверг❤️\n❤️/Пятница❤️')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс,напишите ему:https://t.me/joinchat/YJ0vLNxwSQ41MDBi')
        
        
#@dp.message_handler(commands=['Monday'])
async def commands_monday(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Понедельник:\nПервая пара.\nВысшая математика.\nАудитория №234\nВторая пара.\nТеория Алгоритмов.\nАудитория №263\nТретья пара.\nАнглийский язык.\nАудитория №98\nЧетвертая пара.\nОтсутствует\nПятая пара.\nОбьектно Ориентированное Программировоание')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс,напишите ему:https://t.me/joinchat/YJ0vLNxwSQ41MDBi')
#@dp.message_handler(commands=['Tuesday'])
async def commands_tuesday(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Вторник:\nПервая пара.\nТеория Алгоритмов.\nАудитория №124\nВторая пара.\nДискретная математика.\nАудитория №163\nТретья пара.\nФранцузкий язык.\nАудитория №298\nЧетвертая пара.\nФизика.\nАудитория №200')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс,напишите ему:https://t.me/joinchat/YJ0vLNxwSQ41MDBi')
#@dp.message_handler(commands=['Wednesday'])
async def commands_wednesday(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Среда:\nПервая пара.\nТеория Алгоритмов.\nАудитория №124\nВторая пара.\nДискретная математика.\nАудитория №163\nТретья пара.\nФранцузкий язык.\nАудитория №298\nЧетвертая пара.\nФизика.\nАудитория №200')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс,напишите ему:https://t.me/joinchat/YJ0vLNxwSQ41MDBi')
#@dp.message_handler(commands=['Thursday'])
async def commands_thursday(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Четверг:\nПервая пара.\nТеория Алгоритмов.\nАудитория №124\nВторая пара.\nДискретная математика.\nАудитория №163\nТретья пара.\nФранцузкий язык.\nАудитория №298\nЧетвертая пара.\nФизика.\nАудитория №200')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс,напишите ему:https://t.me/joinchat/YJ0vLNxwSQ41MDBi')
#dp.message_handler(commands=['Friday'])
async def commands_friday(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Пятница:\nПервая пара.\nТеория Алгоритмов.\nАудитория №124\nВторая пара.\nДискретная математика.\nАудитория №163\nТретья пара.\nФранцузкий язык.\nАудитория №298\nЧетвертая пара.\nФизика.\nАудитория №200')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс,напишите ему:https://t.me/joinchat/YJ0vLNxwSQ41MDBi')        
#@dp.message_handler(commands=['list'])
async def commands_list(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Список группы #KU22 : \n1.Бут Богдан\n2.Винтовкин Максим\n3.Голоцван Даниил\n4.Кононенко Михаил\n5.Курдюмов Михаил\n6.Кузинская Екатерина\n7.Нестеренко Никита\n8.Лофицкая Анастасия ')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс,напишите ему:https://t.me/joinchat/YJ0vLNxwSQ41MDBi')
#@dp.message_handler(commands=['news'])
async def commands_news(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Последняя новость:\n 17.11.2021\n 👨‍🎓З Днем студента, Каразінці!👩‍🎓\nБажаємо легкого навчання без зубріння та недосипань, веселих пар із гарними викладачами та смішними історіями, яскравих років студентства з добрими друзями та незабутніми подіями🤗\nНехай студентські роки залишають у серці круті емоції, а навчання не викликає смуток😉Головне, щоб око не смикалося перед заліками та іспитами, а складалися вони автоматом😏\nP.S. Побільше ЗАЧЬОТних моментів у вашому житті👋😎 ')
        await message.delete()
    except:
        await message.reply('Общение с ботом через Лс,напишите ему:https://t.me/joinchat/YJ0vLNxwSQ41MDBi')


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands = ['start', 'help'])
    dp.register_message_handler(commands_timetable, commands = ['Расписание'])
    dp.register_message_handler(commands_monday, commands = ['Понедельник'])
    dp.register_message_handler(commands_tuesday, commands = ['Вторник'])
    dp.register_message_handler(commands_wednesday, commands = ['Среда'])
    dp.register_message_handler(commands_thursday, commands = ['Четверг'])
    dp.register_message_handler(commands_friday, commands = ['Пятница'])
    dp.register_message_handler(commands_list, commands = ['Список'])
    dp.register_message_handler(commands_news, commands = ['Новости'])
