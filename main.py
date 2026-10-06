While True:
    print("MENU OPTIONS")
    print("Please enter the following options to perform the desired action:")
    print("1. Encrypt a message\n2. Decrypt a message\n3. Brute Force Attack\n4. View History\n5. Exit")
    
    # The user will enter the option they want to perform here
    Selected_option = (input("Enter your option: "))
    #=========================================================Variables=========================================================================================
    If Selected_option == 1
    #The user message will be entered here
    message = input("Enter Message:    ").lower()

    #The user will enter the shify key value here
    key = int(input("Enter key value of any length (Please enter only numeric values):   "))


    #Remainder will be shift key vlaue
    shift_key = key % 26

    #Initialize encypted message with empty string
    encrypted_message = ''

    #To hold the decrypted message
    decrypted_message = ''

    #Turn A into its computer number ord(letter)
    #===============================================================Encryption Logic===============================================================================
    #Use for loop go over the individual words from the message variable
    for character in message:
            #print(character)
            #if character == ' ':
                #encrypted_message += " "
            #print(character)
            #checking for non alaphabetic characters which includes, space, commas, question mark
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


    #===============================================================Decryption Logic===============================================================================
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
            

    #Intitializing empty object store the attempts
    brute_force_attempts = {}

    #using  the for loop to go over the the possible attempts from 1-10
    for shift_key in range (1,26): 
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
    for shift, message in brute_force_attempts.items():
                print(f"Shift {shift:2}: {message}")
