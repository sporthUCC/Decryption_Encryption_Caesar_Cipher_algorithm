
#ENCRYPTION CODE
message = "Hello World Hello World Hello World zoo 2026"
#To hold the new encrypted message
encrypted_message = ''

#To hold the decrypted message
decrypted_message = ''

#Tun A into its computer numbernumber = ord(letter)

#Use for loop go over the individual words from the message variable
for character in message:
        print(character)
        #if character == ' ':
            #encrypted_message += " "
        #print(character)
        #checking for non alaphabetic characters which includes, space, commas, question mark
        if character.isalpha():
                #converting each message charater from letters to numbers
                number = ord(character)
                #print(number)

                #adding the shift key to the ASCII number
                next_number = number + 3
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

print(encrypted_message)


for  character in encrypted_message:
    if character.isalpha():
        #converting the character to number/s for calculation
        character_number = ord(character)

        #Subtracting based on the shift key value from the charcter_number
        next_number = character_number -3
        if character.islower() and next_number < 97:
            next_number +=  26
        #converting back to letters
        new_char = chr(next_number)
        decrypted_message += new_char
        
    else:
        '''
        This is for when we need to put the the non letter character back to the orignal position
        '''
        decrypted_message +=character

print(decrypted_message)
        



