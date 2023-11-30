from random import randint
import secrets


def sms_code_generate() -> str:
    random_code = randint(10000, 99999)
    return str(random_code)


def session_token_generate():
    token = secrets.token_hex(32)
    return token
