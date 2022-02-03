with open(".\\Input\\Names\\invited_names.txt", mode="r") as names:
    name_list = names.readlines()

with open(".\\Input\\Letters\\starting_letter.txt", mode="r") as file_entry:
    letter_content = file_entry.read()

for name in name_list:
    stripped_name = name.strip()
    new_letter = letter_content.replace("[name]", stripped_name)
    with open(f".\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)

