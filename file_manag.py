import os 


if os.path.exists("test.txt"):
    print("The file .txt exists")
else:
    print("The file does not exists")
    
    
with open("test.txt", "r") as file:
    content = file.read()


file = open("test.txt", "w")
file.write("localhost: 127.0.0.1")


file = open("test.txt", "r")
content = file.read()

    
file = open("test.txt", "r")
file.close()


