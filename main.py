from morse_code import MORSE_CODE


def convert_to_morse(string):
    string = string.upper()
    morse_string = []
    try:
        [morse_string.append(MORSE_CODE[char]) for char in string]
    except KeyError:
        print("Sorry only alphanumeric values please")
    else:
        return morse_string


string = input("Insert string to convert to morse code: ")
print(convert_to_morse(string))
