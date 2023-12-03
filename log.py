def message(text):
    print(text)
    file = open("log.txt", "a")
    file.write(text)
    file.write("\n")
    file.close()