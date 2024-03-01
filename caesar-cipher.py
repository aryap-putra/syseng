alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encoded_text = ''
    for letter in text:
        letter_index = alphabet.index(letter)
        encoded_text += str(alphabet[(letter_index + shift) % len(alphabet)])
    return encoded_text


def decrypt(text, shift):
    decoded_text = ''
    for letter in text:
        letter_index = alphabet.index(letter)
        decoded_text += str(alphabet[letter_index - shift])
    return decoded_text


def restart(choice):
    global end
    if choice == 'y':
        end = True
    elif choice == 'n':
        end = False
    else:
        print("Please type either 'y' or 'n'.")
        choice = str(input("Do you want to end this program? Type 'y' to end, type 'n' to continue using.\n"))
        restart(choice)
    return end


end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encoded_text = encrypt(text=text, shift=(shift % len(alphabet)))
        print('The encoded text is', encoded_text)
    elif direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decoded_text = decrypt(text=text, shift=(shift % len(alphabet)))
        print('The encoded text is', decoded_text)
    else:
        print("Please type either 'encode' or 'decode'.")

    choice = str(input("Do you want to end this program? Type 'y' to end, type 'n' to continue using.\n"))
    end = restart(choice)
