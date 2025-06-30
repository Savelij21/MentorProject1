from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def get_start_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Поделиться контактом",
                    request_contact=True
                )
            ]
        ],
        resize_keyboard=True,
    )

    return kb



