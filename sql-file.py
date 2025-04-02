from aiogram import Bot, Dispatcher, types
from sqlalchemy.orm import Session

bot = Bot(token='7873713671:AAE1nR-Y52M3SIM-1Df7v9pnqcoPw-Qegm4')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    db: Session = SessionLocal()
    user_state = get_user_state(db, message.from_user.id)
    if not user_state:
        # Create a new user state if it doesn't exist
        new_user_state = UserState(user_id=message.from_user.id, state='initial')
        db.add(new_user_state)
        db.commit()
    await message.answer("Welcome to the bot!")
