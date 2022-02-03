import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_format = {row.letter: row.code for (index, row)
               in nato_data_frame.iterrows()}


def generate_phonetic():
    user_word = input("Write a name: ").upper()
    try:
        user_word_split = [dict_format[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please. ")
        generate_phonetic()
    else:
        print(user_word_split)


generate_phonetic()
