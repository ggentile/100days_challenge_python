alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

code_message = []

def caesar(txt, shift, direction):
    code_txt = ''
    if direction == 'decode':
        shift *= -1
    if shift > len(alphabet):
        new_shift = shift % len(alphabet)
        shift = new_shift
    for letters in txt:
        if letters not in alphabet:
            code_message.append(letters)
        else:
            position = alphabet.index(letters)
            new_position = position + shift
            code_message.append(alphabet[new_position])
        code_txt = ''.join(code_message)
    print(code_txt)
