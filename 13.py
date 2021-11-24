#Create a list of colors from comma-separated color names entered by user. Displayfirst and last colors.

name=input("enter the colors")
list=name.split(",")
print("first color=",list[0])
print("last color=",list[-1])