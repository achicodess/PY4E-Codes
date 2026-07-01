name = input("Enter your name: ")
prompt = input(f"What do you want to discover today, {name}? ").strip().lower()

msg1 = "What is the weather like today??".lower()
msg2 = "How can I improve my company's performance??".lower()
msg3 = "My sales is beggining to pick up, what do I do next??".lower()

if prompt == msg1:
    print("\n--- Weather Mode ---")
    try:
        feel = input("How do you currently feel in your room? (hot / cold / normal): ").strip().lower()
    except:
        print("Invalid input. Try again!")
        feel = ""

    if feel in ["hot", "warm"]:
        print("The weather today seems to be around 30 to 35 degree Celsius.")
    elif feel in ["cold", "chilly"]:
        print("There seems to be a slight dip in temperatures with the current being 15 to 20 degree Celsius.")
    else:
        print("Room temperatures are the best. The temperature now is around 25 to 26 degree Celsius.")

elif prompt == msg2:
    print("\n--- Company Improvement Mode ---")
    data = input("Please tell me more about your company: ")
    try:
        with open("sample.txt", "w") as obj:   
            obj.write(data)
        print("Company details saved to sample.txt")
    except Exception as e:
        print(f"Error saving file: {e}")

elif prompt == msg3:
    print("\nThat is awesome!! Please give me more information on how the progress has been so far.")

else:
    print("Oops. We ran into a problem. We are trying our best to expand the AI's database.")

