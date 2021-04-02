Cryptography chipper module for python


## Installation

```bash
$ python3 -m pip install chipper-chicken
```

##import:

```python
    >>> from chipperchicken import encrypt
    >>> from chipperchicken import decrypt
```

##encrypt:


```python
    >>> e = encrypt(b'data',  'secret', 600)
```

##decrypt:


```python
    >>> decrypt(e, 'secret', 600)
    'data'
```

