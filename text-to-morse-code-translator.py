print(f'''
 _____         _     _          __  __                        ____          _      
|_   _|____  _| |_  | |_ ___   |  \/  | ___  _ __ ___  ___   / ___|___   __| | ___ 
  | |/ _ \ \/ / __| | __/ _ \  | |\/| |/ _ \| '__/ __|/ _ \ | |   / _ \ / _` |/ _ \ 
  | |  __/>  <| |_  | || (_) | | |  | | (_) | |  \__ \  __/ | |__| (_) | (_| |  __/
  |_|\___/_/\_\\__|   \__\___/  |_|  |_|\___/|_|  |___/\___|  \____\___/ \__,_|\___|
''')
print('Hello there!')

#dictionary representing the morse code chart
morse_code_dict = { 'A':'.-', 'B':'-...',
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
                    '(':'-.--.', ')':'-.--.-' }

# function to encode text to morse code
def to_morse_code(text):
    morse_code = ''
    for char in text:
        # checking for space
        # to add single space after every character and slash after every word
        if char == ' ':
            morse_code += ' / '
        else:
            # adding encoded morse code to the result
            morse_code += morse_code_dict[char.upper()] + ' '
    return morse_code

morse_code = to_morse_code(input('Write a sentence to transform in Morse Code: '))
print(f'The result is: {morse_code}')

