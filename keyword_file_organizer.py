import os
import re
import shutil

def get_user_input():
    """
    Prompts the user for the directory path and keyword-subdirectory mappings.
    Returns the directory path and a dictionary of keyword-subdirectory mappings.
    """
    directory = input("Enter the directory path: ")
    mappings = {}
    while True:
        keyword = input("Enter a keyword (or press Enter to finish): ")
        if not keyword:
            break
        subdirectory = input(f"Enter the subdirectory for keyword '{keyword}': ")
        mappings[keyword] = subdirectory
    return directory, mappings

def scan_directory(directory):
    """
    Scans the specified directory and its subdirectories for files.
    Returns a list of file paths.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def extract_keywords(file_name, mappings):
    """
    Extracts keywords from the file name using regular expressions.
    Returns a list of matched keywords.
    """
    keywords = []
    for keyword in mappings.keys():
        if re.search(keyword, file_name, re.IGNORECASE):
            keywords.append(keyword)
    return keywords

def organize_files(directory, file_paths, mappings):
    """
    Organizes the files into subdirectories based on the matched keywords.
    Moves the files to the appropriate subdirectories and handles naming conflicts.
    Returns a dictionary of organized files and their destinations.
    """
    organized_files = {}
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        keywords = extract_keywords(file_name, mappings)
        if keywords:
            subdirectory = mappings[keywords[0]]
            destination_dir = os.path.join(directory, subdirectory)
            os.makedirs(destination_dir, exist_ok=True)
            destination_path = os.path.join(destination_dir, file_name)
            if os.path.exists(destination_path):
                new_file_name = f"{os.path.splitext(file_name)[0]}_copy{os.path.splitext(file_name)[1]}"
                destination_path = os.path.join(destination_dir, new_file_name)
            shutil.move(file_path, destination_path)
            organized_files[file_path] = destination_path
    return organized_files

def generate_summary_report(organized_files):
    """
    Generates a summary report of the organized files and their destinations.
    Prints the report to the console.
    """
    print("Summary Report:")
    print("---------------")
    for source, destination in organized_files.items():
        print(f"Moved: {source} -> {destination}")

def main():
    try:
        directory, mappings = get_user_input()
        file_paths = scan_directory(directory)
        organized_files = organize_files(directory, file_paths, mappings)
        generate_summary_report(organized_files)
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
