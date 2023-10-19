import random

def generate(length):
    character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-"
    password = ""
    for _ in range(length):
        password += random.choice(character)
    return password

length = int(input("Enter the length : "))
password = generate(length)

print("Generated Password:", password)
