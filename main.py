import random
letters = "АБВГДЕЖИКЛМНОПРСТУФХЦЧШЭЮЯ"
numbers = "123456789"

letters_cod = ""
numbers_cod = ""

for i in range(0, 3):
    letters_cod += random.choice(letters)

for i in range(0, 8):
    numbers_cod += random.choice(numbers)
    if len(numbers_cod) == 3:
        numbers_cod += "."
    if len(numbers_cod) == 6:
        numbers_cod += "."

print(f"{letters_cod} {numbers_cod}")