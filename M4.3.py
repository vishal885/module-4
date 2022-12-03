#Write a Python program to append text to a file and display the text.
file=open("tops.txt","a")
file.write("welcome to python appended mode")
file.close()
print("file appended successfully")
print("*"*50)

file=open("tops.txt","r")
print(file.read())
file.close()