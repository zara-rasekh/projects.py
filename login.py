stored_password="1381"
users={
 
 "niloo":"1381",
 "zara":"2002",
 "marry":"1234"
}

entered_username=input("please enter your username: ")

while entered_username not in users:
   entered_username=input("oh,you are not our users. please try again: ")

   
entered_password=input("please enter your password: ")


if entered_username in users:
    
    while stored_password!=entered_password :
     entered_password=input("oops,your password is wrong. please try again: ")

    print("you loged in successfully")

 
