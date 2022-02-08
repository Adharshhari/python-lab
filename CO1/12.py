#Accept a file name from user and print extension of that.

name=input("Enter the filename with extension:")
a=name.split(".")
print("file extension=" +a[-1])