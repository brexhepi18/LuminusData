def Auto(mode_choice):
    
    Auto_choice = 0
    
    while(Auto_choice != 3):
        print("choose 1 for night mode or 2 for custom and for return to menu")
        Auto_choice = input("Enter a number: ")
        Auto_choice = int(Auto_choice)
        if Auto_choice == 1:
            print("giving priority to the battery")
        elif Auto_choice == 2:
            print("custom mode")
        elif Auto_choice == 3:  
            break  
        else:
            print("invalid input") 
