# HexCodeGeneratorApp

HexCodeGeneratorApp is a simple graphical user interface (GUI) application written in Python using the `tkinter` library. It converts a user's name into a unique 12-digit hexadecimal code and displays corresponding glyph images for each digit. This README provides instructions on how to build and use the application.

## Features

- Convert any name into a unique 12-digit hexadecimal code.
- View and copy the generated code.
- Explore glyph images for each digit.

## Prerequisites

- Python (>=3.6)
- Tkinter (usually included with Python)
- Pip (for package installation)

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/HexCodeGeneratorApp.git
    cd HexCodeGeneratorApp
    ```

2. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```
    python app.py
    ```

2. The GUI window will appear. Follow the on-screen instructions to use the application:
    - Enter a name in the input field.
    - Click the "Convert" button to generate the hexadecimal code and view glyph images.
    - Click the "Copy Hex Code" button to copy the code to the clipboard.
    - Click the "Clear" button to reset input and output fields.

3. To close the application, simply close the GUI window.

## Customization

- You can customize the background image and icon by replacing the files in the `customization` and `data` folders, respectively.
- Glyph images are loaded from the `glyphs` directory. You can add or replace these images as needed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Credits

- Created by: [Your Name]
- Special thanks to: [Contributors or acknowledgments]

## License

This project is licensed under the [MIT License](LICENSE).
