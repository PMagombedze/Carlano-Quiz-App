import re

commonPasswords = [
    123456,
    'password',
    123456789,
    12345678,
    12345,
    1234567,
    'admin',
    123123,
    'qwerty',
    'abc123',
    'letmein',
    'monkey',
    111111,
    'password1',
    'qwerty123',
    'dragon',
    1234,
    'baseball',
    'iloveyou',
    'trustno1',
    'sunshine',
    'princess',
    'football',
    'welcome',
    'shadow',
    'superman',
    'michael',
    'ninja',
    'mustang',
    'jessica',
    'charlie',
    'ashley',
    'bailey',
    'passw0rd',
    'master',
    'love',
    'hello',
    'freedom',
    'whatever',
    'nicole',
    'jordan',
    'cameron',
    'secret',
    'summer',
    '1q2w3e4r',
    'zxcvbnm',
    'starwars',
    'computer',
    'taylor',
    'startrek',
    123456,
    123456789,
    'qwerty',
    'password',
    12345,
    'qwerty123',
    '1q2w3e',
    12345678,
    111111,
    1234567890
]

def is_secure_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"\d",password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]",password):
        return False
    if password in commonPasswords:
        return False    
    return True
