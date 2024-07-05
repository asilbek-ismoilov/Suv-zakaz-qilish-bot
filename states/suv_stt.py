from aiogram.fsm.state import State, StatesGroup

class Zakazqilish(StatesGroup):
    name = State()
    surname = State()
    tel = State()
    location = State()
    sav_son = State()