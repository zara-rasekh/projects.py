password=input("please enter your password: ")

def passw(password):
  
  if len(password)<8:
     print("your password must be at least 8 char")
  elif password.isnumeric():
     print("your password must have at least one letter")
  elif password.isalpha():
     print("your password must have at least one number")
  else:
     print("your password is correct")


while True:
 
  passw(password)

     