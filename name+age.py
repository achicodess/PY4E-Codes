name = input("Enter name: ")
age = int(input("Enter age: "))

if age >= 18:
    print("Welcome to our website", name)
else:
    print("Website only for adults as it contains research and deeply informative content.")
    quit()

while True:  
    print("\nOption 1: Create a file")
    print("Option 2: Write to the file")
    print("Option 3: Exit")
    
    try:
        opt = int(input("Enter an option from 1-3: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if opt == 1:
        try:
            with open("sample.txt", "w") as obj:
                print("File creation successful! You can now use Option 2.")
        except Exception as e:
            print("Error creating file:", e)

    elif opt == 2:
        try:
            content = input("Enter content here: ")
            with open("sample.txt", "a") as obj:
                obj.write(content + "\n")
            print("Content written successfully!")
        except Exception as e:
            print("Error writing to file:", e)

    elif opt == 3:
        print("Exiting Application.....")
        break
    else:
        print("Invalid option! Please choose 1, 2, or 3.")

print("Program execution successful.")