morse_codes = {
    'A':'.-', 'B':'-...',
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

choice = int(input("Enter 0 to Encrypt or Enter 1 decrypt a string: "))

if choice == 0:
    s = input("Enter a string to convert it to morse code: ")
    encoded_s = ""
    s = s.upper()

    for i, e in enumerate(s):
        if e == ' ':
            encoded_s += ' '
        else:
            encoded_s += morse_codes[e]
        encoded_s += ' '

    print("Morse code for the string is:", encoded_s)

else:
    list_keys = list(morse_codes.keys())
    list_vals = list(morse_codes.values())

    s = input("Enter encoded string to decode it: ")
    s.strip()
    decoded_s = ""
    words = s.split("  ")

    for word in words:
        letters = word.split()
        for letter in letters:
            decoded_s += list_keys[list_vals.index(letter)]
        decoded_s += ' '

    print(decoded_s)



