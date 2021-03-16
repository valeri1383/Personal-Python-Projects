lookup = {'a': 'aaaaa', 'b': 'aaaab', 'c': 'aaaba', 'd': 'aaabb', 'e': 'aabaa',
          'f': 'aabab', 'g': 'aabba', 'h': 'aabbb', 'i': 'abaaa', 'j': 'abaab',
          'k': 'ababa', 'l': 'ababb', 'm': 'abbaa', 'n': 'abbab', 'o': 'abbba',
          'p': 'abbbb', 'q': 'baaaa', 'r': 'baaab', 's': 'baaba', 't': 'baabb',
          'u': 'babaa', 'v': 'babab', 'w': 'babba', 'x': 'babbb', 'y': 'bbaaa',
          'z': 'bbaab'}


''' Bacon encrypting function '''
def encrypt_with_bacon(text):
    cipher = ''
    for letter in text:
        if letter != ' ':
            cipher += lookup[letter]
        else:
            cipher += ' '
    return cipher


''' Bacon decrypting function '''
def decrypt_with_bacon(text):
    decipher = ''
    i = 0

    while True:
        if i < len(text) - 4:
            substr = text[i:i + 5]
            if substr[0] != ' ':
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
                i += 5
            else:
                decipher += ' '
                i += 1
        else:
            break
    return decipher


''' Caesar encrypting function '''
def encrypt_with_caesar(text, symbol):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += ' '
        elif char.isupper():
            result += chr((ord(char) + symbol - 65) % 26 + 65)
        else:
            result += chr((ord(char) + symbol - 97) % 26 + 97)
    return result


''' Caesar decrypting function '''
def decrypt_with_caesar(text, symbol):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += ' '
        elif char.isupper():
            result += chr((ord(char) - symbol - 65) % 26 + 65)
        else:
            result += chr((ord(char) - symbol - 97) % 26 + 97)
    return result



''' User interface '''

action = input('What would you like to do encrypt/decrypt? ')

if action == 'encrypt':
    method = input('Which method would you like to use caesar/bacon? ')
    if method == 'caesar':
        text_for_encrypting = input('Please enter your text for encrypting: ')
        symbol = int(input('Please enter your encrypting number: '))
        result_from_caesar_encrypting = (encrypt_with_caesar(text_for_encrypting, symbol))
        print(result_from_caesar_encrypting)
    elif method == 'bacon':
        text_for_encrypting = input('Please enter your text for encrypting: ')
        result_from_beacon_encrypting = (encrypt_with_bacon(text_for_encrypting))
        print(result_from_beacon_encrypting)
    else:
        print('Please user correct method !!!')


elif action == 'decrypt':
    method = input('Which method would you like to use caesar/beacon? ')
    if method == 'caesar':
        text_for_decrypting = input('Please enter your text for decrypting: ')
        symbol = int(input('Please enter your decrypting number: '))
        result_from_caesar_decrypting = (decrypt_with_caesar(text_for_decrypting, symbol))
        print(result_from_caesar_decrypting)
    elif method == 'bacon':
        text_for_decrypting = input('Please enter your text for decrypting: ')
        result_from_bacon_decrypting = (decrypt_with_bacon(text_for_decrypting))
        print(result_from_bacon_decrypting)
    else:
        print('Please user correct method !!!')
else:
    print('Please enter correct details !!!')





