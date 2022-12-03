#Write a Python program to copy the contents of a file to another file.
file3=open("file3.txt","r")
file4=open("file4.txt","a")
for line in file3:
    file4.write(line)
    print("done")
file3.close()
file4.close()