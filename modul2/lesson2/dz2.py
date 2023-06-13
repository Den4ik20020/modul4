from telebot import TeleBot
import requests
from bs4 import BeautifulSoup
import random
from telebot.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

bot = TeleBot(token="5929082062:AAEpQTlPpiaZ7A87yxUq6eBjA0Z20xTIAAA")
BASE_FILES_DIR = r"D:\Kod\modul 2\lesson2\extra"


def create_welcome_keyboard():
    welocme_keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button_1 = KeyboardButton("/cats")
    button_2 = KeyboardButton("/poem")
    button_3 = KeyboardButton("/music")
    button_4 = KeyboardButton("/sticker")
    button_5 = KeyboardButton("/game")
    welocme_keyboard.add(button_4, button_3, button_1, button_2, button_5)
    return welocme_keyboard

def create_genre_keyboard():
    welocme_keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button_1 = KeyboardButton("/cats")
    button_2 = KeyboardButton("/poem")
    button_3 = KeyboardButton("/music")
    button_4 = KeyboardButton("/sticker")
    button_5 = KeyboardButton("/game")
    genre_keyboard.add(button_4, button_3, button_1, button_2, button_5)
    return genre_keyboard

@bot.message_handler(commands=['start', 'help'])
def welocme(message: Message):
    welocme_keyboard = create_welcome_keyboard()
    bot.send_message(message.from_user.id, "Привет, выбери команду!", reply_markup=welocme_keyboard)


@bot.message_handler(commands=['cats'])
def cats(message: Message):
    random_img_number = random.randint(1, 9)
    random_img = open(rf"{BASE_FILES_DIR}\{random_img_number}.jpg", "rb")
    bot.send_photo(message.from_user.id, random_img)


@bot.message_handler(commands=['music'])
def music(message: Message):
    audio = open(rf"{BASE_FILES_DIR}\happy.mp3", "rb")
    bot.send_audio(message.from_user.id, audio)


@bot.message_handler(commands=['poem'])
def poem(message: Message):
    bot.send_message(message.from_user.id, "Села муха на варенье, вот и всё стихотворенье.")
    poem_keyboad = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Перейти", url="https://stihi.ru/")
    poem_keyboad.add(button)
    bot.send_message(message.from_user.id, "Больше стихотворений зедсь:", reply_markup=poem_keyboad)


@bot.message_handler(commands=['sticker'])
def sicker(message: Message):
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEG6idjoeVTeanGbS4OqFFv4fRwGoqIuQACRCYAAm42EEl-TAZZKR0X_CwE")


@bot.message_handler(commands=['game'])
def game(message: Message):
    response = requests.get("https://randomgeeks.ru/generator-games/random/?id=1443")
    soup = BeautifulSoup(response.text, "html.parser")
    game = soup.find(class_="under-ad-horizontal-name")
    game_text = game.text
    bot.send_message(message.from_user.id, game_text)


bot.polling()
