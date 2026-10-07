session_history = []
#===============================================MAIN LOOP STARTS===================================================
while True:
    print("=========================MENU OPTIONS============================")
    print("Please enter a the following options to perform the desired action:")
    print("1. Encrypt a message\n2. Decrypt a message\n3. Brute Force Attack\n4. View History\n5. Exit")
    print("==================================================================")
    #===============================================INNER LOOP FOR ERROR HANDLING==============================================
    #This keeps prompting the user until they enter numeric text value
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
        while True:
            message = input("\nEnter Message to Encrypt: ")
            if message.strip() == "":
                print('\nError: Cannot be empty. Please enter text')
            else:
                #exit loop once True
                break        
        #Prompts the user to enter a correct input value 
        while True:
            #Executed the user 
            try:
                #The user will enter the shift key value here which encrypts the message)
                key = int(input("\nEnter key value of any length (Please enter only numeric values): "))
                break
            #The will only execute if the value that was entered was a non numeric value
            except ValueError:
                print("\n ERROR:Only numeric values are accepted. Please try again")
        #calculate shift dynamically
        shift_key = key % 26
        encrypted_message = ''
    #Use "for" loop to go over the individual words from the message variable
        for character in message:
            #print(character)
            #This checks for alphabetic character from A-Z; this return a True or False value
            if character.isalpha():
                #Triggers if the letter/s are upperCase A-Z
                if character.isupper():
                    #converts from letter to number
                    number = ord(character)
                    #adding the newly converted interger value to shift key value
                    next_number = number + shift_key
                    '''check if the nect nmber is creater than 90 if creater than 90 
                       it substract 26 from it to reset the value; wraps it back around '''
                    if next_number > 90:
                        next_number -=26
                    #converts the interger value back into strings of text
                    new_char = chr(next_number)
                    encrypted_message += new_char  
                #checker for lowrcase input value 
                elif character.isalpha():
                    #This checks for alphabetic character from a-z; this return a True or False value.
                    if character.islower():
                        #converts from letter to number
                        number = ord(character)
                        next_number = number + shift_key
                        if next_number > 122:
                            next_number -=26
                        new_char = chr(next_number)
                        encrypted_message += new_char      
            else:  
                    '''
                    This is for when we need to put the the non letter character back to the orignal position
                    '''      
                    encrypted_message =  encrypted_message+character

        print(f"Encrypted Message: {encrypted_message}")
        
        #Encryption history
        encryption_history_log = {
            "Operation": "Encryption",
            "Original Message": message,
            "Encrypted Key Value": shift_key,
            "Encrypted Message": encrypted_message
        }
        #adding the encrypted message/s to the session history
        session_history.append(encryption_history_log)
        
        input('\nPress enter to return to the main menu...')
    #===============================================================DECRYPTION LOGIC START===============================================================================
    elif selected_option == 2:
        while True:
            message = input("\nEnter Message to be Decrypt: ")
            if message.strip() == "":
                print('\nError: Cannot be empty. Please enter text')
            else:
                #exit loop once True
                break        
        #Prompts the user to enter a correct input value 
        while True:
            #Executed the user 
            try:
                #The user will enter the shift key value here which encrypts the message)
                key = int(input("\nEnter key value of any length (Please enter only numeric values): "))
                break
            #The will only execute if the value that was entered was a non numeric value
            except ValueError:
                print("\n ERROR:Only numeric values are accepted. Please try again")
                #calculate shift dynamically
        shift_key = key % 26
        decrypted_message = ''
        
        
        for  character in message:
            '''This checks for aphabetic character from A-Z/a-z; this returns True for 
               alphabetic character and False for everything else'''
            
            if character.isalpha():
                if character.isupper():
                    #converts from letters to number
                    number = ord(character)
                    #substracting the newly converted interger value to shift key value
                    next_number = number - shift_key
                    #Wrapping letter upper case letter if it falls below 65
                    if next_number  < 65:
                        next_number +=26
                    new_char = chr(next_number)
                    decrypted_message +=new_char
                    
    
            elif character.islower():
                #converts letter to number
                number = ord(character)
                #Adds the cipher shift key to the integer to slide forward across the alpahbet
                next_number = number + shift_key
                #if the shift falls below 97 (a) it wraps it around
                if next_number < 97:
                    next_number +=26
                new_char = chr(next_number)
                decrypted_message += new_char
                     
            else:
                '''
                This is for when we need to put the the non letter character back to the orignal position
                '''
                decrypted_message +=character
                

        print(f"Decrypted Message: {decrypted_message}")
        
        decryption_history_log = {
            "Operation": "Decryption",
            "Original Message": message,
            "Encrypted Key Value": shift_key,
            "Encrypted Message": decrypted_message      
        }
        
        session_history.append(decryption_history_log)
        
        #Once the user press enter the return to the main menu
        
        input("\nPress Enter to return to menu....")
    
    
    #===============================================================DECRYPTION LOGIC ENDS ===============================================================================            
    
    #================================================================BRUTE FORCE LOGIC STARTS============================================================================
    elif selected_option == 3:
        while True:
            intercepted_message = input("\nEnter Ciphertext Message to Brute Force: ")
            if intercepted_message.strip() == "":
                print("\nError: Cannot be empty. Please enter text: ")
            else:
                break
        #Rest the dictionary to clear out previous attack from the memmory    
        brute_force_attempts = {}
        #using  the for loop to go over the the possible attempts from 1-10
        for attempt_key in range (1,11): 
            #stores the different brute force attempts
            decrypted_attempt = ""
            #print(decrypted_attempt)
            
            for character in intercepted_message:
                if character.isupper():
                    number = ord(character)
                    next_number = number - attempt_key
                    
                    if next_number < 65:
                        next_number += 26
                    new_char = chr(next_number)
                    decrypted_attempt +=new_char
                #Handles the lower case values 
                elif character.islower():
                    character_number = ord(character)
                    next_number = character_number - attempt_key
                    
                    #wrapping alphabet around
                    if next_number < 97:
                        next_number +=26
                    new_char = chr(next_number)
                    decrypted_attempt +=new_char
                else:
                    decrypted_attempt +=character
                    
            brute_force_attempts[attempt_key] = decrypted_attempt
            
        # Display all attempts
        print( "=============================BRUTE FORCE ATTACK (Shift 1-10)===================================== ")

        for rotation, decrypted_message_attempt in brute_force_attempts.items():
                print(f"Key Rotation {rotation:2}: {decrypted_message_attempt}")
        #Why the correct message is easy to put
        print("\n==========================================ANALYSIS================================================")
        print("\nWhy the correct message is easy to spot Analysis:")
        print("As human reader, you will almost immediately recognize real character and patterns.You will only see exactly ONE row that make sense in plain English.")
        print("Depending on what the original shift key value was, that specific rotation line is where the decrypted message will would be located at.")
        print("\n===================================================================================================")
        input("\nPress Enter to return to menu....")
                
            
    #================================================================BRUTE FORCE LOGIC ENDS============================================================================
    
    
    #====================================================================HISTORY START================================================================================= 
    elif selected_option == 4:
        print("\n==========================================SESSION HISTORY================================================")
        
        if(len(session_history)) == 0:
            print("No History has been recorded yet.")
            print('Please Peform action: Select 1 for Encryptpion or Select 2 for Decryption')  
        else:
            print(f"{'No.':<5} | {'Operation':<10} | {'Shift':<6} | {'Original Message':<25} | {'Resulting Output'}")
       
        #====================================================================HISTORY ENDS================================================================================= 

    elif selected_option == 5:
            print("\nExiting Program. Goodbye!!!")
    #else:
        #print("\nInvalid option. Please select between 1-5")
 