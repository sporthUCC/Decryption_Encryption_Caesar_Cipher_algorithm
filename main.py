
#ENCRYPTION CODE
message = "Hello World Hello World Hello World zoo 2026"
#To hold the new encrypted message
encrypted_message = ''

#To hold the decrypted message
decrypted_message = ''

#Tun A into its computer numbernumber = ord(letter)

#Use for loop go over the individual words



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

                #adding the shift key value
                next_number = number + 3
                #converting back into apha/text characters

                '''
                Check for to ensure that the character is lowercase and greater than 122 (122=z this is the highest ASCII code for the lowercase alphabet). If it true the we execute the if block of code.
                The next_number variable is then reassigned to itself and subtracted from 26 since the a-z aplphabet stops at 26.
                '''
                if character.islower() and next_number > 122:
                     next_number -=  26
                new_char = chr(next_number)
                encrypted_message += new_char
               
        else:  
            #provides final answer which includes        
            encrypted_message =  encrypted_message+character

print(encrypted_message)


for  character in encrypted_message:
    if character.isalpha():
        #converting the character to number/s for calculation
        character_number = ord(character)

        #Subtracting based on the shift key value
        next_number = character_number -3

        #converting back to letters
        new_char = chr(next_number)

        decrypted_message += new_char
        
    else:
        decrypted_message +=character

print(decrypted_message)
        



