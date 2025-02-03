# MetaTool

MetaTool is a simple Python program designed to help organize your files and folders by providing batch renaming capabilities. It allows you to add prefixes or suffixes to file names and replace spaces with underscores, making it easier to maintain an organized file structure on Windows systems.

## Features

- Batch rename files in a specified directory.
- Add a prefix or suffix to file names.
- Replace spaces in file names with underscores.
- Option to perform a dry run to preview changes without renaming files.

## Requirements

- Python 3.x

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Download or clone the MetaTool repository to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `metatool.py`.
3. Run the script using Python:

   ```bash
   python metatool.py
   ```

4. Follow the on-screen prompts to specify the directory and renaming options:
   - Enter the directory path where the files are located.
   - Specify a prefix and/or a suffix to add to the file names.
   - Choose whether to replace spaces with underscores.
   - Decide if you want to perform a dry run to preview changes.

## Example

If you have files named `document 1.txt` and `image 2.jpg` in `C:\MyFiles` and you run MetaTool with the following options:

- Prefix: `project_`
- Suffix: `_2023`
- Replace spaces with underscores: Yes

The renamed files would be:

- `C:\MyFiles\project_document_1_2023.txt`
- `C:\MyFiles\project_image_2_2023.jpg`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements or additional features.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).