def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (For example, converting to uppercase)
        modified_content = content.upper()  # You can modify the content as needed
        
        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File content has been successfully modified and written to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read or write the file '{input_filename}'.")

# Ask the user for input and output filenames
input_filename = input("Enter the filename to read from: ")
output_filename = input("Enter the filename to write to: ")

# Call the function to read, modify, and write the file
read_and_modify_file(input_filename, output_filename)
