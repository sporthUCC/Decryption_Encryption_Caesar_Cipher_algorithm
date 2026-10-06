#The user message will be entered here
message = input("Enter Message:  ").lower()
#Initialize encypted message with empty string
encrypted_message = ''
#To hold the decrypted message
decrypted_message = ''
#Initialize brute forc attacks with empty string; this is use to store the value later on in the program
brute_force_attempts = {}

#===============================================ERROR HANDLING FOR INPUT VALUES==============================
#Error handling for incorrect data type
while True:
     #Executed the user 
     try:
        #The user will enter the shift key value here which encrypts the message)
        key = int(input("\nEnter key value of any length (Please enter only numeric values): "))
        break
     #The will only execute if the value that was entered was a non numeric value
     except ValueError:
          print("\n ERROR:Only numeric values are accepted. Please try again")
#===============================================ERROR HANDLING FOR INPUT VALUES==============================

#Remainder will be shift key vlaue
shift_key = key % 26

#===============================================MAIN LOOP===================================================
while True:
    print("=========================MENU OPTIONS============================")
    print("Please enter a the following options to perform the desired action:")
    print("1. Encrypt a message\n2. Decrypt a message\n3. Brute Force Attack\n4. View History\n5. Exit")
    print("==================================================================")
    #===============================================INNER LOOP FOR ERROR HANDLING==============================================
    while True: 
        try:
            # The user will enter the option they want to perform here
            selected_option = int(input("\nEnter your option: ").strip())
            #Checks to see if the input is between 1 and 5, if true it exits the loop
            if selected_option >= 1 and selected_option<=5:
                 break  
            else:
                 #catched number that are less than 1 or greater than 5
                 print("\nError: Invalid selected option. Please select a numeric value from the menu (1-5)")
             
        except ValueError: 
             print("\nERROR: Invalid input. Letter and/or Symbols are not allowed. Please enter numeric value from the menu")
            
    #===============================================================Encryption Logic===============================================================================
    if selected_option == 1:
    #Use for loop go over the individual words from the message variable
        for character in message:
                #print(character)
                #This checks for alphabetic character from A-Z; this return a True or False value
                if character.isalpha():
                        #converting each message charater from letters to numbers
                        number = ord(character)
                        #print(number)
                        #adding the shift key to the ASCII number
                        next_number = number + shift_key
                        '''
                        Check for to ensure that the character is lowercase and greater than 122 (122=z this is the highest ASCII code for the lowercase alphabet). If it true the we execute the if block of code.
                        The next_number variable is then reassigned to itself and subtracted from 26 since the a-z aplphabet stops at 26.
                        '''
                        if character.islower() and next_number > 122:
                            next_number -=  26
                        #converting back into apha/text characters
                        new_char = chr(next_number)
                        encrypted_message += new_char
                    
                else:  
                    '''
                    This is for when we need to put the the non letter character back to the orignal position
                    '''      
                    encrypted_message =  encrypted_message+character

        print(f"Encrypted Message: {encrypted_message}")

    #===============================================================DECRYPTION LOGIC===============================================================================
    elif selected_option == 2:
        for  character in encrypted_message:
            if character.isalpha():
                #converting the character to number/s for calculation
                character_number = ord(character)
                #print( character_number)

                #Subtracting based on the shift key value from the charcter_number
                next_number = character_number - shift_key

                #If the shift goes beyond 97 it wraps it around
                if character.islower() and next_number < 97:
                    next_number += 26
                #converting back to letters
                new_char = chr(next_number)
                decrypted_message += new_char
                
            else:
                '''
                This is for when we need to put the the non letter character back to the orignal position
                '''
                decrypted_message +=character

        print(f"Decrypted Message: {decrypted_message}")
                
    #====================================BRUTE FORCE LOGIC===============================================================
    elif selected_option == 3:
        #using  the for loop to go over the the possible attempts from 1-10
        for attempt_key in range (1,26): 
            #stores the different brute force attempts
            decrypted_attempt = ""
            #print(shift_key)
            for character in encrypted_message:
                if character.isalpha():
                    character_number = ord(character)
                    next_number = character_number - shift_key
                #wrap around alphabet
                    if character.islower() and next_number < 97:
                        next_number += 26
                    decrypted_attempt += chr(next_number)

                else:
                    decrypted_attempt += character

            brute_force_attempts[shift_key] = decrypted_attempt

        # Display all attempts
        print( "BRUTE FORCE ATTACK ")

        for rotation, decrypted_message_attempt in brute_force_attempts.items():
                print(f"Key Rotation {rotation:2}: {decrypted_message_attempt}")

    #====================================HISTORY===============================================================  
    elif selected_option == 4:
         print("History")
    if len(history) == 0:
        print("No history has being recorded here")
        print(Print Encrypt or decrypt a message first.\n")
    else:
        #Print the table headings
        print(f"{'No.':<5}{'Operation':<10}{'Shift':<7}{'Original':<25}{'Result'}")
        print("-" * 80)

        #Loop through each saved record and print it as a row
        for record in history:
            print(f"{record['number']:<5}{record['operation']:<10}{record['shift']:<7}{record['original']:<25}{record['result']}")
            print()

    elif selected_option == 5:
        #ask the user if they want to exit the program
        confirm_exit = input("Are you sure you want to exit? (y/n): ").lower()
        if confirm_exit == 'y':
         print("\nExiting Program. Goodbye!!!")
<<<<<<< HEAD
         break
    elif confirm =='n'
         print("\nReturning to the main menu...")
    else:
         print("\nInvalid option. Please select between 1-5")
=======
         break
>>>>>>> b9c286cb4a6fbf4eae4ecff52e5f9a7f11f4e73e
