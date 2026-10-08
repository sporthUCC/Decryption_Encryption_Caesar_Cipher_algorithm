"""
Cours: ITT212 Python Programming
Assignment: Caesar Cipher Encryption and Decryption System
Academic Year: 2026 - 2027
Lecturer: Mr. Jonathan Johnson
"""

session_history = []
#===============================================MAIN LOOP STARTS===================================================
while True:
    print("-"* 200)
    print("MENU OPTIONS".center(200))
    print("-"* 200)
    print("Please enter a the following options to perform the desired action:")
    print("1. Encrypt a message\n2. Decrypt a message\n3. Brute Force Attack\n4. View History\n5. Exit\n")
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
            
    #===============================================================Cipher Logic Start===============================================================================
    if selected_option in [1,2]:
        
        #Determine the name of of the action / opertion the user want to pwerform
        operation = "Encryption" if selected_option == 1 else "Decryption"
        
        while True:
            #using the f string to be able to place the operation variable inside the input message string
            message = input(f"\nEnter Message to {operation}: ")
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
        #this line converts the shift into a negative number for decryption and keep it as a positive number foe encryption
        final_shift = shift_key if selected_option == 1 else -shift_key
        #use to store decrypted or encrypted message
        cipher_text = ""
    
    #Use "for" loop to go over the individual words from the message variable
        for character in message:
            #print(character)
            #This checks for alphabetic character from A-Z / a-z; this return a True or False value
            if character.isalpha():
                #Triggers if the letter/s are upperCase A-Z
                if character.isupper():
                    #converts from letter to number
                    number = ord(character)
                    #adding the newly converted interger value to final shift key to get the next number in the ASCII
                    next_number = number + final_shift
                    '''check if the nect nmber is creater than 90 if creater than 90 
                       it substract 26 from it to reset the value; wraps it back around '''
                    if next_number > 90:
                        next_number -=26
                         
                    elif next_number< 65:
                        '''
                        This is used to check if the value is less than 65; 65 in the ASCII table is the equivalent of uppercase 'A'. If it is less than 65, 26 would be added to the next number and 
                        wrap the value around. For Example, if the user wanted to decrypt a letter that started with a capital 'A' and a shift of 3, it's going to go below 65, and it's going to be 
                        62 doesn't represent a letter; it represents a symbol.
                        '''    
                        next_number +=26
                    #converts the interger value back into strings of text
                    new_char = chr(next_number)
                    cipher_text += new_char  
                #checker for lowrcase input value 
                elif character.islower():
                    #converts from letter to number
                    number = ord(character)
                    next_number = number + final_shift
                    if next_number > 122:
                        next_number -=26
                    elif next_number < 97:
                        next_number +=26
                    new_char = chr(next_number)
                    cipher_text += new_char      
            else:  
                    '''
                    This is for when we need to put the the non letter character back to the orignal position
                    '''      
                    cipher_text =  cipher_text+character

        #showing the enrypted or decrypted message
        print(f"\n{operation}ed  Result: {cipher_text}")
        
        result_key = "Encrypted Message" if selected_option ==1  else "Decrypted Message"
        
        #Dynamically keep a track of the of the history key name so History in option 4 can read it correctly
        history_log = {
            "Operation": operation,
            "Original Message": message,
            "Encrypted Key Value": shift_key,
             result_key: cipher_text
        }
        #adding the encrypted message/s to the session history
        session_history.append(history_log)
        
        input('\nPress enter to return to the main menu...')
    #===============================================================Cipher Logic ends===================================================================================           
    
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
        print("-"*200)
        print( "BRUTE FORCE ATTACK (Shift 1-10)".center(200))
        print("-"*200)
        for rotation, decrypted_message_attempt in brute_force_attempts.items():
                print(f"Key Rotation {rotation:2}: {decrypted_message_attempt}")
        #Why the correct message is easy to identify while using the caesar cipher algorithm
        print("-"*200)
        print("ANALYSIS".center(200))
        print("-"*200)
        print("""
        Why the correct message is easy to spot Analysis:
        
        As human reader, you will almost immediately recognize real character and patterns.You will only see exactly ONE row that make sense in plain English.
        Depending on what the original shift key value was, that specific rotation line is where the decrypted message will would be located at.Furthermore, 
        a key limitation of the Caesar Cipher is that all possible decrypted messages retain the exact same length, making pattern analysis much 
        easier compared to advanced modern encryption methods for e.g AES.")
        """)
        
        print("\n===========================================================================================================================================")
        input("\nPress Enter to return to menu....")
                
            
    #================================================================BRUTE FORCE LOGIC ENDS============================================================================
    
    
    #====================================================================HISTORY START================================================================================= 
    elif selected_option == 4:
        print("="*200)
        #Aligning session history in the missle
        print("SESSION HISTORY".center(200))
        print("="*200)
        
        #check to see if the session history list is empty. If it is empty it return a message, if is not empty then it show the history of the session
        if session_history == []:
            print("[!]No History has been recorded yet.")
            print('Please Peform an action: Select 1 for Encryptpion or Select 2 for Decryption')  
        else:
            #Formatting Header using string formatter
            print(f"{'No.':<5}|{'Operation':<10}|{'Shift':<6}|{'Original Message':<25}|{'Resulting Output'}")
            #printing table divider using - * 90
            print("="*200)
            
            for index, record in enumerate(session_history, start=1):
                #print(index, record)
                history_log_result = record["Encrypted Message"] if record["Operation"] == "Encryption" else record["Decrypted Message"]
                #shows the the history result based on the action we carried out, whether that's decryption or encryption
                print(f"{index:<5}|{record['Operation']:<10}|{record['Encrypted Key Value']:<6}|{record['Original Message']:<25}|{history_log_result} ")
                print("="*200)
                
        input("\nPress Enter to return to menu....")
                
        #====================================================================HISTORY ENDS================================================================================= 

    elif selected_option == 5:
            print("\nSession Completed. Goodbye!!!")
            break
 