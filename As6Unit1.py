import base64

text = 'MDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDEwMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDExMDAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAxMDAxMTAwMTEwMDExMDExMQ=='


def decodeBase64(base64_decode):
    text = base64.b64decode(base64_decode)
    binary = (str(text)).strip("b'")  # b'00110011 => 00110011
    return binary


def binaryHex(text):
    s = hex(int(text, 2))  # convert binary to hex
    hexa = ''
    for i in range(2, len(s), 4):  # 0x33 37 33 32 33 383335333 => 373238
        hexa += s[i + 2:i + 4]
    return hexa


def hexDecimal(text):
    hexa = str(text)
    deci = ''
    for i in range(1, len(hexa), 2):  # 37323835313230 => 72 85 120
        deci += hexa[i]
    return deci


def decodeRot13(text):
    deci = str(text)
    s = ''
    i = 0
    while i < len(deci):
        num = deci[i:i + 2]
        if int(num) >= 32:
            s += chr(int(num))              # 72 85 120 48 => H U x 0
            i += 2
        else:                                # HUx0H0I7LwEmZ19wZT52Z3W0Z3WsZwL1ZwW9
            num = deci[i:i + 3]
            s += chr(int(num))
            i += 3
    rot13 = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    return s.translate(rot13)


bin = decodeBase64(text)
print(bin)
hex = binaryHex(bin)
print(hex)
dec = hexDecimal(hex)
print(dec)
rot13 = decodeRot13(dec)
print(rot13)
flag = (decodeBase64(rot13))
print(flag)