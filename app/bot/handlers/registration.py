import logging
import re

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.bot.keyboards import cancel_keyboard, main_menu_keyboard, phone_keyboard, remove_keyboard
from app.bot.states import RegistrationStates
from app.services.user_service import UserService

logger = logging.getLogger(__name__)

router = Router(name="registration")


@router.message(RegistrationStates.first_name, F.text == "❌ Cancel")
@router.message(RegistrationStates.last_name, F.text == "❌ Cancel")
@router.message(RegistrationStates.phone_number, F.text == "❌ Cancel")
async def cancel_registration(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Registration cancelled. Send /start when you're ready to try again.",
        reply_markup=remove_keyboard(),
    )


@router.message(RegistrationStates.first_name, F.text)
async def process_first_name(message: Message, state: FSMContext) -> None:
    first_name = message.text.strip()
    if len(first_name) < 2 or len(first_name) > 100:
        await message.answer(
            "Please enter a valid first name (2–100 characters).",
            reply_markup=cancel_keyboard(),
        )
        return

    await state.update_data(first_name=first_name)
    await state.set_state(RegistrationStates.last_name)
    await message.answer(
        f"Great, {first_name}! 👋\n\nNow please enter your <b>last name</b>:",
        reply_markup=cancel_keyboard(),
    )


@router.message(RegistrationStates.last_name, F.text)
async def process_last_name(message: Message, state: FSMContext) -> None:
    last_name = message.text.strip()
    if len(last_name) < 2 or len(last_name) > 100:
        await message.answer(
            "Please enter a valid last name (2–100 characters).",
            reply_markup=cancel_keyboard(),
        )
        return

    await state.update_data(last_name=last_name)
    await state.set_state(RegistrationStates.phone_number)
    await message.answer(
        "Almost done! 📱\n\nPlease share your <b>phone number</b> using the button below:",
        reply_markup=phone_keyboard(),
    )


@router.message(RegistrationStates.phone_number, F.contact)
async def process_phone_contact(
    message: Message,
    state: FSMContext,
    user_service: UserService,
) -> None:
    contact = message.contact
    if contact.user_id != message.from_user.id:
        await message.answer(
            "Please share your own phone number.",
            reply_markup=phone_keyboard(),
        )
        return

    await _complete_registration(message, state, user_service, contact.phone_number)


@router.message(RegistrationStates.phone_number, F.text)
async def process_phone_text(
    message: Message,
    state: FSMContext,
    user_service: UserService,
) -> None:
    phone = message.text.strip()
    if not re.match(r"^\+?[0-9\s\-()]{7,20}$", phone):
        await message.answer(
            "Please enter a valid phone number (e.g. +998901234567) or use the share button.",
            reply_markup=phone_keyboard(),
        )
        return

    await _complete_registration(message, state, user_service, phone)


async def _complete_registration(
    message: Message,
    state: FSMContext,
    user_service: UserService,
    phone_number: str,
) -> None:
    data = await state.get_data()
    await user_service.register_user(
        telegram_id=message.from_user.id,
        first_name=data["first_name"],
        last_name=data["last_name"],
        phone_number=phone_number,
    )
    await state.clear()
    logger.info("User registered: telegram_id=%s", message.from_user.id)
    await message.answer(
        "✅ Registration complete!\n\n"
        "You can now browse visa requirements for Latvia, Slovakia, Germany, "
        "Poland, and the United Kingdom.",
        reply_markup=main_menu_keyboard(),
    )
