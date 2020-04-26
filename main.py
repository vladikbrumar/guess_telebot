import telebot
import random

bot = telebot.TeleBot('1249282954:AAGCIOBsizfrXk4E4a0S0mhllJnJFcjAVVY')


def fill_array():
    array = [i + 1 for i in range(100)]
    return array


def first_num():
    number = random.randint(0, 100)
    return number


number_range = fill_array()
low = 0
high = len(number_range)
middle = first_num()

# keyboard /start
keyboardYesNo = telebot.types.ReplyKeyboardMarkup()
keyboardYesNo = telebot.types.ReplyKeyboardMarkup(True, True)
keyboardYesNo.row('Да', 'Нет')

# keyboard picking number
keyboardReady = telebot.types.ReplyKeyboardMarkup()
keyboardReady = telebot.types.ReplyKeyboardMarkup(True, True)
keyboardReady.row('Готово')

# keyboard guessing number
keyboardAsk = telebot.types.ReplyKeyboardMarkup()
keyboardAsk = telebot.types.ReplyKeyboardMarkup(True, True)
keyboardAsk.row('Больше', 'В яблочко!', 'Меньше')

# keyboard ask new attempt
keyboardAgain = telebot.types.ReplyKeyboardMarkup()
keyboardAgain = telebot.types.ReplyKeyboardMarkup(True, True)
keyboardAgain.row('Снова', 'Хватит!')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, дававй сыграем в игру?', reply_markup=keyboardYesNo)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Загадай число от 1 до 100', reply_markup=keyboardReady)
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Очень жаль, что ты на столько злой!')

    if message.text.lower() == 'готово':
        bot.send_message(message.chat.id, 'Ты загадал ' + str(check_number()) + ' ?', reply_markup=keyboardAsk)

    if message.text.lower() == 'больше':
        it_more()
        bot.send_message(message.chat.id, 'Ты загадал ' + str(check_number()) + ' ?', reply_markup=keyboardAsk)
    elif message.text.lower() == 'меньше':
        it_less()
        bot.send_message(message.chat.id, 'Ты загадал ' + str(check_number()) + ' ?', reply_markup=keyboardAsk)

    if message.text.lower() == 'в яблочко!':
        bot.send_message(message.chat.id, 'ха-ха, я угадал твое число, это ' + str(check_number()),
                         reply_markup=keyboardAgain)
        do_it_again()

    if message.text.lower() == 'снова':
        bot.send_message(message.chat.id, 'Загадай число от 1 до 100', reply_markup=keyboardReady)
    elif message.text.lower() == 'хватит!':
        bot.send_message(message.chat.id, 'Очень жаль, а ведь было весело')


def check_number():
    global number_range, low, high, middle

    guess = number_range[middle]
    return guess


def do_it_again():
    global number_range, low, high, middle
    number_range = fill_array()
    low = 0
    high = len(number_range)
    middle = first_num()


def it_more():
    global low, middle
    low = middle + 1
    middle = (low + high) // 2


def it_less():
    global high, middle
    high = middle - 1
    middle = (low + high) // 2


bot.polling()
