from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

questions_router = Router()


class Questionnaire(StatesGroup):
    name = State()
    gender = State()
    age = State()
    fav_body = State()
    fav_race = State()
    fav_brand = State()
    dream_car = State()


@questions_router.message(Command('stop'))
@questions_router.message(F.text == 'stop')
async def stop_questions(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("The survey is stopped")


@questions_router.message(Command('questions'))
async def start_quest(message: types.Message, state: FSMContext):
    await state.set_state(Questionnaire.name)
    await message.answer("For stopping type 'stop' ")
    await message.answer('What is your name?')


@questions_router.message(F.text, Questionnaire.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(Questionnaire.age)
    await message.answer("How old are you?")


@questions_router.message(F.text, Questionnaire.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text.strip()
    if not age.isdigit():
        await message.answer("Your age should be a number")
    elif int(age) < 12 or int(age) > 100:
        await message.answer("Your age should be between 12 and 100")
    else:
        await state.update_data(age=int(age))

    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Male"),
                types.KeyboardButton(text="Female")
            ]
        ]
    )
    await state.set_state(Questionnaire.gender)
    await message.answer('Your gender?', reply_markup=kb)


@questions_router.message(F.text, Questionnaire.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)

    await state.set_state(Questionnaire.fav_brand)
    await message.answer("What is your favorite car brand", reply_markup=types.ReplyKeyboardRemove())


@questions_router.message(F.text, Questionnaire.fav_brand)
async def process_fav_brand(message: types.Message, state: FSMContext):
    await state.update_data(fav_brand=message.text)

    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Estate"),
                types.KeyboardButton(text="Sedan")
            ],
            [
                types.KeyboardButton(text="Coupe"),
                types.KeyboardButton(text="Hatchback")
            ],
            [
                types.KeyboardButton(text="Cabriolet"),
                types.KeyboardButton(text="SUV")
            ]
        ],
        resize_keyboard=True
    )
    await state.set_state(Questionnaire.fav_body)
    await message.answer("Your favourite car body", reply_markup=kb)


@questions_router.message(F.text, Questionnaire.fav_body)
async def process_fav_body(message: types.Message, state: FSMContext):
    await state.update_data(fav_body=message.text)

    await state.set_state(Questionnaire.fav_race)
    await message.answer("What is your favourite car racing", reply_markup=types.ReplyKeyboardRemove())


@questions_router.message(F.text, Questionnaire.fav_race)
async def process_fav_race(message: types.Message, state: FSMContext):
    await state.update_data(fav_race=message.text)

    await state.set_state(Questionnaire.dream_car)
    await message.answer("Your dream car")


@questions_router.message(F.text, Questionnaire.dream_car)
async def process_dream_car(message: types.Message, state: FSMContext):
    await state.update_data(dream_car=message.text)

    data = await state.get_data()
    print(data)
    await message.answer("Thank you for answering the questions!")
