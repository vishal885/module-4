#Write python program that user to enter only odd numbers, else will raise an exception.
try:
    num=int(input("Enter only odd number :"))
    if num%2!=0:
        print("number id odd")
    else:
        raise Exception("number is Even")
except Exception as e:
    print("Exception Caught :",e)
