def modify_file_content():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Here we Try to open and read the file
        with open(input_file, "r") as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: The file could not be read or written.")

# Run the function
modify_file_content()
