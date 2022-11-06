file= open("Day24_Files_Directories_&_paths\my_file.txt","r") # r for read mode,
contents= file.read()
print(contents)
file.close() # close the file

# another way to open a file
with open("Day24_Files_Directories_&_paths\my_file.txt") as file:
    contents= file.read()
    print(contents) # this will automatically close the file

# write to a file
with open("Day24_Files_Directories_&_paths\my_file.txt", mode="a") as file: # a for append mode
    file.write("\nPizza is the best food ever")

# write to a file
with open("Day24_Files_Directories_&_paths\my_file.txt", mode="w") as file: # w for write mode
    file.write("Love is the best feeling ever")

# if you want to create a new file and write to it use mode="w"
with open("Day24_Files_Directories_&_paths\my_file2.txt", mode="w") as file: # w for write mode
    file.write("Amo a mi familia")