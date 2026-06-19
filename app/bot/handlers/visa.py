import logging

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from app.bot.keyboards import (
    country_keyboard,
    main_menu_keyboard,
    requirement_actions_keyboard,
    visa_type_keyboard,
)
from app.services.user_service import UserService
from app.services.visa_service import VisaService

logger = logging.getLogger(__name__)

router = Router(name="visa")


@router.message(F.text == "🌍 Browse Visa Requirements")
async def browse_visa_requirements(
    message: Message,
    user_service: UserService,
    visa_service: VisaService,
) -> None:
    if not await user_service.is_registered(message.from_user.id):
        await message.answer("Please register first using /start")
        return

    countries = await visa_service.get_countries()
    if not countries:
        await message.answer(
            "No visa data available yet. Please contact support or try again later."
        )
        return

    await message.answer(
        "🌍 Select a <b>country</b> to view visa requirements:",
        reply_markup=country_keyboard(countries),
    )


@router.message(F.text == "👤 My Profile")
async def show_profile(message: Message, user_service: UserService) -> None:
    user = await user_service.get_user(message.from_user.id)
    if user is None:
        await message.answer("Please register first using /start")
        return

    await message.answer(
        f"👤 <b>Your Profile</b>\n\n"
        f"Name: {user.first_name} {user.last_name}\n"
        f"Phone: {user.phone_number}\n"
        f"Telegram ID: {user.telegram_id}",
        reply_markup=main_menu_keyboard(),
    )


@router.callback_query(F.data == "back:countries")
async def back_to_countries(callback: CallbackQuery, visa_service: VisaService) -> None:
    countries = await visa_service.get_countries()
    await callback.message.edit_text(
        "🌍 Select a <b>country</b> to view visa requirements:",
        reply_markup=country_keyboard(countries),
    )
    await callback.answer()


@router.callback_query(F.data == "back:menu")
async def back_to_menu(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer(
        "🏠 Main menu — choose an option:",
        reply_markup=main_menu_keyboard(),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("country:"))
async def select_country(callback: CallbackQuery, visa_service: VisaService) -> None:
    country_id = int(callback.data.split(":")[1])
    country = await visa_service.get_country(country_id)
    if country is None:
        await callback.answer("Country not found.", show_alert=True)
        return

    visa_types = await visa_service.get_visa_types()
    await callback.message.edit_text(
        f"🌍 <b>{country.name}</b>\n\nSelect a <b>visa type</b>:",
        reply_markup=visa_type_keyboard(visa_types, country_id),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("visa:"))
async def show_visa_requirement(callback: CallbackQuery, visa_service: VisaService) -> None:
    _, country_id_str, visa_type_id_str = callback.data.split(":")
    country_id = int(country_id_str)
    visa_type_id = int(visa_type_id_str)

    requirement = await visa_service.get_visa_requirement(country_id, visa_type_id)
    if requirement is None:
        await callback.answer(
            "Visa information not available for this combination.",
            show_alert=True,
        )
        return

    text = visa_service.format_requirement(requirement)
    text += (
        "\n\n⚠️ <i>This information is for guidance only. "
        "Requirements may change — always verify with the official embassy.</i>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=requirement_actions_keyboard(country_id),
    )
    await callback.answer()
