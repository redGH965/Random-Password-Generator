import random
import string

def generate_password(length, use_digits, use_letters, use_special):
    if length < 1:
        raise ValueError("Длина пароля должна быть больше 0")

    chars = ''
    if use_digits:
        chars += string.digits
    if use_letters:
        chars += string.ascii_letters
    if use_special:
        chars += string.punctuation

    if not chars:
        raise ValueError("Выберите хотя бы один тип символов")

    return ''.join(random.choices(chars, k=length))
