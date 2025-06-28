# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)
with open("../Days/Text_files/my_file.txt", "a") as file:
    file.write("New content added to the file.\n")
