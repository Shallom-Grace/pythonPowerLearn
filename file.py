def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        # Read the original file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Define a new filename for the modified file
        new_filename = f"modified_{filename}"

        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read or write to the file '{filename}'.")

# Run the function
read_and_modify_file()
