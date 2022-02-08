#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly

s=input("enter the string \n")
if len(s)>=3:
    if s[-3:]=="ing":
         print(s+"ly")
    else:
        print(s+"ing")
        
           
        
            
        


