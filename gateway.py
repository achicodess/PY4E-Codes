print("Welcome")
print("x-- Login & Register System --x")

user_ids = []
user_passwords = []

while True:
    choice = input("\nDo you want to Login, Register, or Exit? ").lower()
    
    if choice == "login":
        print("\nx--- Login ---x")
        user_id = int(input("Enter userid: "))
        user_pass = int(input("Enter password: "))
        
        if user_id in user_ids:
            
            index = user_ids.index(user_id)
            if user_passwords[index] == user_pass:
                print("Login Successful! Welcome back.")
            else:
                print("Incorrect password. Please try again.")
        else:
            print("User not found. Please register first.")
            
    elif choice == "register":
        print("\nx--- Register ---x")
        new_id = int(input("Enter your userid (Numbers only): "))
        
        
        if new_id in user_ids:
            print("User ID already exists! Try logging in instead.")
        else:
            new_pass = int(input("Enter your password (Numbers only): "))
            user_ids.append(new_id)
            user_passwords.append(new_pass)
            print("Registration Successful! You can now log in.")
            
    elif choice == "exit":
        print("Program Terminated. Restart to access it once again.")
        break
    else:
        print("Invalid choice. Please type 'Login', 'Register', or 'Exit'.")