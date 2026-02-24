
string: str = "Hello"
with open("storage.txt", "a") as file:
    file.write(string)