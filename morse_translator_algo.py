
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher

def decrypt(message):
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


def convertCiphers(message):
    cipher_list =[]
    temp_list = []
    for char_index in range(len(message)):
        temp_list = []
        letter = message[char_index]
        if letter == '?':
            if cipher_list:
                for each_string in cipher_list:
                    a = each_string[:char_index] + '.' + each_string[char_index + 1:]
                    b = each_string[:char_index] + '-' + each_string[char_index + 1:]
                    temp_list.append(a)
                    temp_list.append(b)
                cipher_list = temp_list
            else:
                a = message[:char_index]+'.'+message[char_index+1:]
                b = message[:char_index] + '-' + message[char_index + 1:]
                cipher_list.append(a)
                cipher_list.append(b)

    return cipher_list

def possibilities(message):
    count_que = message.count('?')
    my_list = []
    if count_que:
        msgs = convertCiphers(message)
        for each_msg in msgs:
            result = decrypt(each_msg)
            my_list.append(result) 
        return my_list
    else:
        result = decrypt(message)
        my_list.append(result) 
        return my_list

