__doc__ = """Cryptography


import:
    >>> from chipperchicken import encrypt
    >>> from chipperchicken import decrypt


encrypt:

    >>> e = encrypt(b'data',  'secret', 60000)

decrypt:

    >>> decrypt(e, 'secret', 60000)
    'data'

Author: Madhava-mng
"""
from chipperchicken import encrypt, decrypt
