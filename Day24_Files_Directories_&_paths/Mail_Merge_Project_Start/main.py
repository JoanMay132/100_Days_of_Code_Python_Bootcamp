#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER="[name]"

with open("Input/Names/invited_names.txt") as invited_names: 
    names= invited_names.readlines()
    print(names)

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter= starting_letter.read()
    print(letter)
    for name in names:
        stripped_name= name.strip()
        new_letter= letter.replace(PLACEHOLDER,stripped_name)
        print(new_letter)
        with open(f"Output/ReadyToSend/letter_for{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)
