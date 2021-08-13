import os

try:
    os.mkdir("new")   
except Exception as e:
    print("Error:", e)

os.rmdir("new")

print(os.getcwd()) ##show where are you