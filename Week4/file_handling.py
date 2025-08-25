# Assignment: File Handling & Exception Handling

def modify_file(input_file, output_file):
    """Reads content from input_file, modifies it, and writes to output_file."""
    try:
        # Open input file for reading
        with open(input_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        # Modify each line (uppercase + line numbers)
        modified_lines = [f"{i+1}: {line.strip().upper()}\n" for i, line in enumerate(lines)]

        # Write modified content to new file
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.writelines(modified_lines)

        print(f"✅ Successfully wrote {len(modified_lines)} lines to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ask the user for a filename
    filename = input("📂 Enter the filename to read: ")

    # Define output file
    output_file = "output_modified.txt"

    # Call function
    modify_file(filename, output_file)
