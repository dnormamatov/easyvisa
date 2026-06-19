from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🌍 Browse Visa Requirements")],
            [KeyboardButton(text="👤 My Profile")],
        ],
        resize_keyboard=True,
    )


def country_keyboard(countries: list) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=country.name, callback_data=f"country:{country.id}")]
        for country in countries
    ]
    buttons.append([InlineKeyboardButton(text="◀️ Back to Menu", callback_data="back:menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def visa_type_keyboard(visa_types: list, country_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text=visa_type.name,
                callback_data=f"visa:{country_id}:{visa_type.id}",
            )
        ]
        for visa_type in visa_types
    ]
    buttons.append(
        [InlineKeyboardButton(text="◀️ Back to Countries", callback_data="back:countries")]
    )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def requirement_actions_keyboard(country_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="◀️ Other Visa Types",
                    callback_data=f"country:{country_id}",
                )
            ],
            [InlineKeyboardButton(text="🌍 Other Countries", callback_data="back:countries")],
            [InlineKeyboardButton(text="🏠 Main Menu", callback_data="back:menu")],
        ]
    )
