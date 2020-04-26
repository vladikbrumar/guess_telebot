import random
import numpy as np


def random_num():
    number = random.randint(0, 100)
    return number


def fill_array():
    # working..
    # array = np.empty(0)
    # for i in range(100):
    #     array = np.append(array, i+1)

    array = [i+1 for i in range(100)]
    return array


def output_array(array):
    for i in range(len(array)):
        print(array[i])


output_array(fill_array())

#  if message.text.lower() == 'больше':
#     bot.send_message(message.chat.id, check_number(message), reply_markup=keyboardAsk)
# elif message.text.lower() == 'меньше':
#     bot.send_message(message.chat.id, check_number(message), reply_markup=keyboardAsk)
# elif message.text.lower() == 'в яблочко!':
#     bot.send_message(message.chat.id, check_number(message), reply_markup=keyboardAsk)


# @bot.message_handler(content_types=['text'])
# def check_number(message):
#     global number_range, low, high, middle
#
#     guess = number_range[middle]
#     bot.send_message(message.chat.id, 'do you guess ' + str(guess), reply_markup=keyboardAsk)
#     if message.text.lower == 'в яблочко!':
#         return 'your number is' + str(guess)
#     elif message.text.lower == 'больше':
#         low = middle + 1
#     elif message.text.lower == 'меньше':
#         high = middle - 1
#
#     return 'None'
