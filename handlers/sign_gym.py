from aiogram.filters.state import StateFilter
from aiogram import F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from model import *
from database import Database,ClientTable,TrainingTable

# Регистрация Клиента

class Registration(StatesGroup): # Состояние
    name_input = State()
    phone_number_input = State()
    date_training_input = State()
    training_time_input = State()
    type_training_input = State()
    

router = Router()

@router.message(StateFilter(None), Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(text="Здравствуйте, это спортзал SHPI" 
                              "Запишитесь в зал SHPI на любую дату уже на первую тренеровку! Введите команду /register",)

@router.message(StateFilter(None), Command('register'))
async def register(message: Message, state: FSMContext):
    await message.answer(text="Введите Имя>>")
    await state.set_state(Registration.name_input)

@router.message(Registration.name_input, F.text.regexp(r'^[А-Я][а-я]+$'))
async def name_input(message: Message, state: FSMContext):
    data = await state.get_data()
    data['name'] = message.text.lower()
    await state.update_data(name=data['name'])
    await message.answer(text="Введите ваш номер телефона, в виде +7..........>>>>")
    await state.set_state(Registration.phone_number_input)
    
@router.message(Registration.name_input)
async def invalid_name_input(message: Message, state: FSMContext):
    await message.answer(text="Имя должно начинаться с заглавной буквы и состоять только из русских символов!")



@router.message(Registration.phone_number_input,F.text.regexp(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'))
async def phone_input(message: Message, state: FSMContext):
    data = await state.get_data()
    data['phone_number'] = message.text.lower()
    await state.update_data(phone_number=data['phone_number'])
    
    name = data.get('name')
    phone_number = data.get('phone_number')
    print(name)
    print(phone_number)
    
    Database.open(
             host='109.206.169.221', 
             user='seschool_01', 
             password='seschool_01', 
             database='seschool_01_pks1')
    
    ClientTable.add(name,phone_number)
      
    await message.answer("Клиент успешно добавлен!")




    await message.answer(text="Введите дату тренеровки, в виде ГГГГ-ММ-ДД>>>>")
    await state.set_state(Registration.date_training_input)

@router.message(Registration.phone_number_input)
async def invalid_phone_number_input(message: Message,state: FSMContext):
    await message.answer(text="Телефоный номер должен начинаться с +7 и 10 цифрами:"
    "пример: +79999999999")


@router.message(Registration.date_training_input,F.text.regexp(r'^\d{4}-\d{2}-\d{2}$'))
async def date_training_input(message: Message,state: FSMContext):
    data = await state.get_data()
    data["date_training"] = message.text.lower()
    await state.update_data(date_training=data['date_training'])
    await message.answer(text="Введите время тренеровки, в виде часы:минуты>>")
    await state.set_state(Registration.training_time_input)


@router.message(Registration.date_training_input)
async def invalid_date_training_input(message: Message, state: FSMContext):
     await message.answer(text="Дата неверная! Она должна быть корректной! \n"
                               "Пример: 2025-02-12")

@router.message(Registration.training_time_input,F.text.regexp(r'^(0?[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$'))
async def time_training_input(message: Message,state: FSMContext):
    data = await state.get_data()
    data["time_training"] = message.text.lower()
    await state.update_data(time_training=data['time_training']) 
    await message.answer(text="Введите тип тренеровки из указанных вариантов: Кардио, Йога, Силовые>>>")
    await state.set_state(Registration.type_training_input)             

@router.message(Registration.training_time_input)
async def invalid_time_training_input(message: Message, state: FSMContext):
    await message.answer(text="Время неверное! Оно должно быть корректным!  \n"
                              "Пример: 12:15")
    

@router.message(Registration.type_training_input,F.text.regexp(r'^(Кардио|Силовая|Йога)$'))
async def type_training(message: Message,state: FSMContext):
    data = await state.get_data()
    data['type_training'] = message.text.lower()
    await state.update_data(type_training=data['type_training'])

    date_training = data.get('date_training')
    time_training = data.get('time_training')
    type_training = data.get("type_traning")
    
    
    Database.open(
             host='109.206.169.221', 
             user='seschool_01', 
             password='seschool_01', 
             database='seschool_01_pks1')
    
    TrainingTable.add(date_training,time_training,type_training)
      
    await message.answer("Тренеровка успешно добавлена!")

    
   

    await message.answer(text="Регистрация завершена!")
    



@router.message(Registration.type_training_input)
async def invalid_type_training_input(message: Message, state: FSMContext):
    await message.answer(text="Тип тренеровки неверный! Можно указать лишь эти 3 варианта с заглавном буквой! \n"
                              "Пример: Кардио")
    
    
