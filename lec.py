def info(name, age):
    print(f"Name: {name}, Age: {age}")
info("Amina", 20)

def student(name, age=18):
    print(f"Name: {name}, Age: {age}")
student("Amina")
student("Amina", 19)