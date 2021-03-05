from Cryptodome.Cipher import AES


def _decrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=text[:16])
    msg = cipher.decrypt(text[16:])
    return msg

def read_content(user_data, database):
    try:
        record = database.get_content(user_data['USER_LOGIN'])
        text = _decrypt(record, user_data['USER_SECRET'])
        return text
    except:
        return 'ERROR'

