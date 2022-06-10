
print (""" This program converts milliseconds into hours, minutes, and seconds\n
To exit the program, please type 'exit' """)

value= input("Please enter the milliseconds (should be greater than zero) :  ")
def convert(value):
    hours = int(int(value) / (1000*60*60))%24
    minutes =int (int(value) / (1000*60))%60
    seconds = int(int(value) / 1000)%60
    
    if  hours!=0 and minutes !=0 and seconds !=0:
        return (f"{hours} hour/s, {minutes} minute/s,{seconds} second/s" )
    elif  hours==0 and minutes !=0 and seconds !=0:
        return (f"{minutes} minute/s,{seconds} second/s" )
    elif  hours!=0 and minutes ==0 and seconds ==0:
        return (f"{hours} hour/s" )
    elif  hours==0 and minutes ==0 and seconds !=0:
        return (f"{seconds} second/s" )
    elif  hours==0 and minutes !=0 and seconds ==0:
        return (f"{minutes} minute/s" )
    elif  hours!=0 and minutes ==0 and seconds !=0:
        return (f"{hours} hour/s, {seconds} second/s" )
    elif  hours!=0 and minutes !=0 and seconds ==0:
        return (f"{hours} hour/s, {minutes} minute/s" )
    elif int(value) < 1000:
        return (f"Just {value} millisecond/s")
       
       
while True:
    
    if value.lower() == "exit":
        break
    
    elif value.isdecimal() == False:
        print (" Your input is invalid")
        print (" Please enter a valid number")
        value= input("Please enter the milliseconds (should be greater than zero) :  ")
        
    elif int(value) < 1:
         print (" Your input is invalid")
         print (" Please enter a valid number")
         value= input("Please enter the milliseconds (should be greater than zero) :  ")
 
    else: 
        print(convert(value))
        break
