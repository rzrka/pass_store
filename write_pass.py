from Cryptodome.Cipher import AES

def padding_text(text):
    pad_len = (16 - len(text) % 16) % 16
    return text + b' ' * pad_len

def _encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(text)
    return ciphertext


def write_content(user_data):
    user_data['USER_MESSAGE'] = padding_text(user_data['USER_MESSAGE'])
    user_data['USER_MESSAGE'] = _encrypt(user_data['USER_MESSAGE'], user_data['USER_SECRET'])

