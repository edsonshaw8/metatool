import os

def rename_files_in_directory(directory, prefix='', suffix='', replace_spaces=False, dry_run=True):
    """
    Renames files in the specified directory by adding a prefix, suffix, or replacing spaces with underscores.

    :param directory: The target directory containing files to rename.
    :param prefix: A string to add at the beginning of each file name.
    :param suffix: A string to add at the end of each file name (before the file extension).
    :param replace_spaces: If True, replaces spaces in the file names with underscores.
    :param dry_run: If True, only prints the changes without renaming the files.
    """
    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                # Split the filename and its extension
                name, ext = os.path.splitext(filename)
                new_name = name
                
                # Add prefix and suffix
                new_name = f"{prefix}{new_name}{suffix}"
                
                # Replace spaces with underscores if requested
                if replace_spaces:
                    new_name = new_name.replace(' ', '_')
                
                # Create the new filename
                new_filename = f"{new_name}{ext}"
                
                # Display the changes or rename the file
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                
                if dry_run:
                    print(f"Would rename: {old_file_path} to {new_file_path}")
                else:
                    print(f"Renaming: {old_file_path} to {new_file_path}")
                    os.rename(old_file_path, new_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Example usage
    directory = input("Enter the directory path: ")
    prefix = input("Enter the prefix (leave blank if not needed): ")
    suffix = input("Enter the suffix (leave blank if not needed): ")
    replace_spaces = input("Replace spaces with underscores? (yes/no): ").lower() == 'yes'
    dry_run = input("Perform a dry run? (yes/no): ").lower() == 'yes'

    rename_files_in_directory(directory, prefix, suffix, replace_spaces, dry_run)

if __name__ == "__main__":
    main()