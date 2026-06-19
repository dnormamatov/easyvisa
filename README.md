# EasyVisa

Telegram bot MVP that helps Uzbek users understand visa requirements for different countries.

## Stack

- Python 3.12+ (tested on 3.14 with prebuilt wheels)
- aiogram 3.x
- PostgreSQL (Supabase)
- SQLAlchemy 2.x (async + asyncpg)
- Alembic
- python-dotenv

## Features

- User registration (first name, last name, phone number)
- Three visa types: Student, Tourist, Work
- Five countries: Latvia, Slovakia, Germany, Poland, United Kingdom
- Visa details: required documents, application process, processing time, estimated costs

## Project Structure

```
easyvisa/
├── app/
│   ├── bot/              # Telegram handlers, keyboards, states, middlewares
│   ├── config/           # Settings and environment configuration
│   ├── data/             # Seed data for countries and visa requirements
│   ├── domain/           # Domain enums and entities
│   ├── infrastructure/   # Database models, session, repositories
│   ├── services/         # Business logic layer
│   └── main.py           # Application entry point
├── alembic/              # Database migrations
├── scripts/              # Utility scripts (seed, connection test)
├── alembic.ini
├── requirements.txt
└── .env.example
```

## Setup

1. **Clone and create virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

2. **Configure environment**

   Copy `.env.example` to `.env` and fill in your values:

   ```bash
   cp .env.example .env
   ```

   - `BOT_TOKEN` — from [@BotFather](https://t.me/BotFather)
   - `DATABASE_URL` — Supabase PostgreSQL connection string (`postgresql://` or `postgresql+asyncpg://`)

3. **Test database connection (optional)**

   ```bash
   python -m scripts.test_db_connection
   ```

4. **Run migrations** (also runs automatically on bot startup)

   ```bash
   alembic upgrade head
   ```

5. **Seed visa data**

   ```bash
   python -m scripts.seed
   ```

6. **Start the bot**

   ```bash
   python -m app.main
   ```

## Bot Flow

1. `/start` — welcome message and registration check
2. If not registered — collect first name, last name, phone number
3. Main menu — browse visa requirements by country and type
4. View detailed visa information

## License

MIT
