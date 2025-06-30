from aiogram import Bot, F, Router
from aiogram.enums import ContentType
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, User as TgUser
from sqlalchemy import select

from database import async_session
from keyboards import get_start_keyboard
from models import User

# HANDLERS ------------------------------------------------------
router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot):

    tg_user: TgUser = message.from_user

    async with async_session() as session:

        stmt = select(User).where(User.tg_id == tg_user.id)
        result = await session.execute(stmt)
        db_user: User | None = result.scalar_one_or_none()

        if db_user is None:
            return await message.answer(
                text="Вас еще нет в базе. Поделитесь вашим контактом для аутентификации 👇",
                reply_markup=get_start_keyboard()
            )

    return await message.answer("Вы успешно авторизовались в системе!")


@router.message(F.contact)
async def process_contact(message: Message, bot: Bot):

    tg_user: TgUser = message.from_user

    async with async_session() as session:

        print(message.contact.phone_number)

        stmt = select(User).where(User.phone == message.contact.phone_number)
        result = await session.execute(stmt)
        db_user: User | None = result.scalar_one_or_none()

        if db_user is None:
            return await message.answer(
                text="Вашего номера телефона нет в базе данных. В доступе отказано.",
                reply_markup=ReplyKeyboardRemove()
            )

        db_user.tg_id = tg_user.id
        await session.commit()
        return await message.answer(
            text="Вы успешно авторизовались в системе!",
            reply_markup=ReplyKeyboardRemove()
        )


