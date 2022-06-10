print("This program converts milliseconds into hours, minutes, and seconds")
print("To exit the program, please type 'Exit!'")


def timeConv(n):
 
    seconds = (n / 1000)%60
    minutes =(n / 60000)%60
    hours =  (n / 3600000)%24
    # if hours <= 0 and not minutes <= 0 and not seconds <= 0: 
    #     return  minutes, seconds
    # if minutes <= 0 and not hours <= 0 and not seconds <= 0:
    #     return  hours, seconds
    # if seconds <= 0 and not hours <= 0 and not minutes <= 0:
    #     return  hours, minutes 
    # else:
    return hours,minutes ,seconds          
while True:
    n=input("Enter time in milliseconds  :")
    if n == "Exit":
        print("Exiting this program GOOD BY!")
        break
   
  
    elif n.isdigit()==False or int(n)<=0:
        print("not valid!!")
        print("Please enter a valid time in milliseconds")
    else:
        n=int(n) 
        print("your given milli second is = ",timeConv(n))

        break 