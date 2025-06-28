# Mail Merge Project
with open("Input/Letters/starting_letter.txt") as file:
    content = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()
# Create the output directory if it doesn't exist
import os

if not os.path.exists("Output/ReadyToSend"):
    os.makedirs("Output/ReadyToSend")

for name in names:
    stripped_name = name.strip()
    new_letter = content.replace("[name]", stripped_name)
    with open(f"Output/ReadyToSend/{stripped_name}.txt", "w") as file:
        file.write(new_letter)
