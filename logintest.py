import time

username = "Aiman"
password = "secretpassword"

username_input = input("Username: ")
password_input = input("Password: ")

if username_input == username and password_input == password:
    print("Access granted")
    print("Please wait")
    time.sleep(5)
    print("Um please wait... Loading...")
    time.sleep(1)
    print("...still Loading XD")
    time.sleep(1)
    print("...")
    print("Alright you have security clearance. Pulling up the secret mainframe.")
elif username_input == username and password_input != password:
    print("Password incorrect")
elif username_input != username and password_input == password:
    print("Username incorrect")
else:
    print("You might wanna check both fields...")
