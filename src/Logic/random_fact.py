from random import choice
from .spreadsheet import spreadsheet

def random_fact():
    'Факты о космосе'
    sheet = spreadsheet('Факты о космосе')
    fact = choice(sheet.get_all_values())
    return fact[0]