# Keyword-Based File Organizer

The Keyword-Based File Organizer is a Python script that helps you organize files in a directory based on user-defined keywords. It allows you to specify a directory path and a set of keywords associated with specific subdirectories. The script then scans the directory for files, extracts keywords from the file names, and moves the files into the corresponding subdirectories based on the matched keywords.

## Features

- User-friendly command-line interface for specifying the directory path and keyword-subdirectory mappings.
- Efficient scanning of the directory and its subdirectories to identify files.
- Keyword extraction from file names using regular expressions.
- Creation of subdirectories based on the specified keywords if they don't already exist.
- Moving files to the appropriate subdirectories while handling potential naming conflicts.
- Generating a summary report of the organized files and their destinations.
- Error handling for invalid directory paths, file permission issues, and other exceptional cases.

## Requirements

- Python 3.x
- OS-specific requirements (if any)

## Usage

1. Clone the repository or download the `keyword_file_organizer.py` script.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command: python keyword_file_organizer.py

4. Follow the prompts to specify the directory path and keyword-subdirectory mappings.

5. The script will scan the directory, organize the files based on the provided keywords, and generate a summary report.

6. Review the summary report to see the organized files and their destinations.

## Examples

Here's an example of how to use the Keyword-Based File Organizer:
Enter the directory path: /path/to/your/directory
Enter a keyword (or press Enter to finish): report
Enter the subdirectory for keyword 'report': reports
Enter a keyword (or press Enter to finish): invoice
Enter the subdirectory for keyword 'invoice': invoices
Enter a keyword (or press Enter to finish):
Summary Report:
Moved: /path/to/your/directory/file1_report.pdf -> /path/to/your/directory/reports/file1_report.pdf
Moved: /path/to/your/directory/file2_invoice.xlsx -> /path/to/your/directory/invoices/file2_invoice.xlsx

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## Acknowledgments

- The Python community for providing valuable resources and libraries.
