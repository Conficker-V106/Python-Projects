from logo import Logo
MORSE_CODE_DATA = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   'a': '.-', 'b': '-...',
                   'c': '-.-.', 'd': '-..', 'e': '.',
                   'f': '..-.', 'g': '--.', 'h': '....',
                   'i': '..', 'j': '.---', 'k': '-.-',
                   'l': '.-..', 'm': '--', 'n': '-.',
                   'o': '---', 'p': '.--.', 'q': '--.-',
                   'r': '.-.', 's': '...', 't': '-',
                   'u': '..-', 'v': '...-', 'w': '.--',
                   'x': '-..-', 'y': '-.--', 'z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Text to Morse
def decrypt():
    print("Choice = Text to Morse Code")
    plain_text = input("ENTER TEXT: ")
    morse = " "
    for letters in plain_text:
        if letters != " ":
            morse += MORSE_CODE_DATA[letters] + " "
        else:
            morse += " "
    return morse


# Morse To Text
def encrypt():
    keys_list = list(MORSE_CODE_DATA.keys())
    values_list = list(MORSE_CODE_DATA.values())
    print("Choice = Morse Code To Text")
    morse_code = input("Enter Morse Code with [.(dots) & -(dashes)]: ")
    morse_code = morse_code.split(" ")
    plain_text = ""
    for codes in morse_code:
        if codes == " ":
            plain_text += " "
        else:
            position = values_list.index(codes)
            plain_text += keys_list[position]
    return plain_text

# MAIN CODE


print(Logo)


Close_Program = False
while not Close_Program:
    choice = input("Enter 1 for Text to Morse Code\nEnter 2 for Morse Code to Text\nEnter 'E' to Exit \n:")
    if choice == "1":
        print(decrypt())
    elif choice == "2":
        print(encrypt())
    elif choice == "E":
        Close_Program = True
    else:
        print("Wrong Choice!!! Please Enter Again")

print("BYE BYE")
