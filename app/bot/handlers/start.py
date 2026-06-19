import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.bot.keyboards import cancel_keyboard, main_menu_keyboard
from app.bot.states import RegistrationStates
from app.services.user_service import UserService

logger = logging.getLogger(__name__)

router = Router(name="start")

WELCOME_MESSAGE = (
    "👋 Welcome to <b>EasyVisa</b>!\n\n"
    "I help Uzbek citizens understand visa requirements for:\n"
    "🇱🇻 Latvia · 🇸🇰 Slovakia · 🇩🇪 Germany · 🇵🇱 Poland · 🇬🇧 United Kingdom\n\n"
    "Visa types: Student · Tourist · Work\n\n"
    "Let's get you registered first. Please enter your <b>first name</b>:"
)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext, user_service: UserService) -> None:
    await state.clear()
    is_registered = await user_service.is_registered(message.from_user.id)

    if is_registered:
        user = await user_service.get_user(message.from_user.id)
        await message.answer(
            f"Welcome back, <b>{user.first_name}</b>! 👋\n\n"
            "Use the menu below to browse visa requirements or view your profile.",
            reply_markup=main_menu_keyboard(),
        )
        return

    await state.set_state(RegistrationStates.first_name)
    await message.answer(WELCOME_MESSAGE, reply_markup=cancel_keyboard())


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        "<b>EasyVisa Help</b>\n\n"
        "/start — Start or restart the bot\n"
        "/help — Show this help message\n\n"
        "<b>How to use:</b>\n"
        "1. Register with your name and phone number\n"
        "2. Tap <b>Browse Visa Requirements</b>\n"
        "3. Select a country and visa type\n"
        "4. View documents, process, timing, and costs\n\n"
        "⚠️ Information is for guidance only. Always verify with official embassy sources.",
    )
