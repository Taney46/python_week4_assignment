def modify_file_content(content):
    """
    Modify the content of the file. For this example,
    we'll convert the text to uppercase.
    """
    return content.upper()

def main():
    try:
        # Ask the user for the filename to read
        input_filename = input("Enter the name of the file to read: ")
        
        # Open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Ask for a new filename to write the modified content
        output_filename = input("Enter the name of the file to write to: ")
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"File has been successfully written to {output_filename}.")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You don't have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
