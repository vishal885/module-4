#Write a Python program to write a list to a file.
names = ["vishal","komal","nisha"]
file=open("vishal3.txt","w")
for item in names:
    file.write("%s\n"%item)
    print("done")
