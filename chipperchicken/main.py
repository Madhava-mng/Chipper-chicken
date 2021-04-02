from base64 import b64encode as _b64enc, b64decode as _b64dec
from codelib.rot import rot13IterForword as _rot13
from codelib.rot import rot13IterBackword as _rot13d
from hashlib import sha1 as _sha256
from random import randint as _rint, choice as _choice

def check_order(ordering):
    if(ordering < 0):
        return check_order(300000 + ordering)
    if(ordering > 300000):
        return check_order(ordering - 300000)
    return ordering

def ran_num(str_):
    hash_ = _sha256(str_.encode()).hexdigest()
    tmp = 0
    for i in hash_:
        if(i.isdigit()):
            tmp += int(i)
        else:
            tmp -= len(str_)
        if(tmp <= 0):
            tmp += len(hash_)//2
    return tmp



def encrypt(bstring, passwd="@#$", rotate=412):
    """
    >>> encrypt(b'str', 'secret', 420)
    """
    r_tmp = chr(_rint(7, 17))
    for i in range(len(bstring)):
        if(i%2 == 0):
            r_tmp += chr(check_order(ord(bstring.decode()[i]) + rotate))
        elif(i%3 == 0):
            r_tmp += chr(check_order(ord(bstring.decode()[i]) - rotate))
        elif(i%5 == 0):
            r_tmp += chr(check_order(ord(bstring.decode()[i]) - rotate))
        elif(i%7 == 0):
            r_tmp += chr(check_order(ord(bstring.decode()[i]) - rotate))
        else:
            r_tmp += chr(check_order(ord(bstring.decode()[i]) + rotate))
    r_tmp += chr(_rint(7, 17))
    r_tmp += chr(_rint(7, 17))
    return _rot13(_b64enc(r_tmp.encode()).decode(), ran_num(passwd)).encode()

def decrypt(bstring, passwd="@#$", rotate=412):
    """
    >>> decrypt(b'IE/B==', 'secure', 540)
    """
    r_tmp = ''
    bstring = _b64dec(_rot13d(bstring.decode(), ran_num(passwd)).encode())[1:-2]

    for i in range(len(bstring.decode())):
        if(i%2 == 0):
            r_tmp += chr(check_order(ord(bstring.decode()[i]) - rotate))
        elif(i%3 == 0):
            r_tmp += chr(check_order(ord(bstring.decode()[i]) + rotate))
        elif(i%5 == 0):
            r_tmp += chr(check_order(ord(bstring.decode()[i]) + rotate))
        elif(i%7 == 0):
            r_tmp += chr(check_order(ord(bstring.decode()[i]) + rotate))
        else:
            r_tmp += chr(check_order(ord(bstring.decode()[i]) - rotate))
    return r_tmp.encode()


