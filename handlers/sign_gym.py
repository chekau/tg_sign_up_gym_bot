from aiogram.filters.state import StateFilter
from aiogram import F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from model import *
# Регистрация Клиента

class Registration(StatesGroup): # Состояние
    name_input = State()
    date_training_input = State()
    training_time_input = State()
    street_input = State()
    house_number_input = State()
    number_input = State()

router = Router()

@router.message(StateFilter(None), Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(text="Здравствуйте, это спортзал SHPI"
                              "Запишитесь в зал SHPI на любую дату уже на первую тренеровку! Введите команду /register",)

@router.message(StateFilter(None), Command('register'))
async def register(message: Message, state: FSMContext):
    await message.answer(text="Введите Имя!")
    await state.set_state(Registration.name_input)

@router.message(Registration.name_input, F.text.regexp(r'^[А-Я][а-я]+$'))
async def name_input(message: Message, state: FSMContext):
    new_user = Client()
    new_user.name = message.text.lower()
    await state.update_data(name=new_user.name)
    await message.answer(text="Введите дату тренеровки")
    await state.set_state(Registration.date_training_input)

@router.message(Registration.name_input)
async def invalid_name_input(message: Message, state: FSMContext):
    await message.answer(text="Имя должно начинаться с заглавной буквы и состоять только из русских символов!")

@router.message(Registration.date_training_input,F.text.regexp(r'^[А-Я][а-я]+$'))
async def date_training_input(message: Message,state: FSMContext):
    data = await state.get_data()
    data["number"] = message.text.lower()
    await state.set_state(Registration.number_input)
    await state.update_data(address=data['date_training'])
    await message.answer(text="Введите время тренеровки")
    await state.set_state(Registration.training_time_input)


@router.message(Registration.date_training_input)
async def invalid_date_training_input(message: Message, state: FSMContext):
    ...

@router.message(Registration.training_time_input,F.text.regexp((r'^[1-9][0-9]*$')))
async def time_training_input(message: Message,state: FSMContext):
    ...                

    