import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar
from PIL import Image, ImageTk
import sys
import os


class HexCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("N2G Generator")
        self.page = None

        # Set the initial window size here
        initial_width = 908
        initial_height = 677
        self.root.geometry(f"{initial_width}x{initial_height}")

        # Load glyph images
        self.load_glyphs()

        # Create notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create pages
        self.create_convert_page()
        self.create_Info_page()

        # Prevent window resizing
        self.root.resizable(False, False)

        self.load_icon()

        # Set focus to the name entry field
        self.name_entry.focus_set()

        # Bind Enter key press event to name entry field
        self.name_entry.bind("<Return>", self.enter_key_pressed)

        self.root.mainloop()

    def load_background(self):
        background_path = os.path.join(
            sys._MEIPASS, "data", "customization", "background.png"
        )
        if os.path.exists(background_path):
            background_image = Image.open(background_path)
            self.background_photo = ImageTk.PhotoImage(background_image)
            self.background_label = tk.Label(self.root, image=self.background_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def load_glyphs(self):
        self.glyphs = {}
        glyph_prefixes = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
        ]

        for prefix in glyph_prefixes:
            image_path = os.path.join(
                sys._MEIPASS, "data", "glyphs", f"Glyph_{prefix}.png"
            )
            try:
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image.thumbnail((64, 64))
                    self.glyphs[prefix] = ImageTk.PhotoImage(image)
            except Exception as e:
                print(f"Error loading image for prefix {prefix}: {e}")

    def create_convert_page(self):
        page = ttk.Frame(self.notebook)
        self.notebook.add(page, text="Convert")

        # Load background image if available
        background_path = os.path.join(
            sys._MEIPASS, "data", "customization", "background.png"
        )
        if os.path.exists(background_path):
            background_image = Image.open(background_path)
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = ttk.Label(page, image=background_photo)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = background_photo  # Keep a reference to the image
        else:
            page.configure(
                style="LightGray.TFrame"
            )  # Set a light gray background style

        # Name input
        ttk.Label(page, text="Enter a name to convert:").grid(
            row=0, column=0, columnspan=2, padx=10, pady=10
        )

        self.name_entry = ttk.Entry(page)
        self.name_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))

        # Convert, Clear, and Copy buttons
        ttk.Button(page, text="Convert", command=self.convert_to_hexadecimal).grid(
            row=2, column=0, padx=10, pady=5, sticky="e"
        )
        ttk.Button(page, text="Clear", command=self.clear_fields).grid(
            row=2, column=1, padx=10, pady=5, sticky="w"
        )
        ttk.Button(page, text="Copy Hex Code", command=self.copy_to_clipboard).grid(
            row=3, column=0, columnspan=2, padx=10, pady=5
        )

        # Output text box
        self.output_text = tk.StringVar()
        output_label = ttk.Label(
            page,
            textvariable=self.output_text,
            wraplength=200,
            justify="left",
            anchor="w",
        )
        output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 0))

        # Center the elements within the area
        page.grid_rowconfigure(0, weight=0)
        page.grid_rowconfigure(1, weight=0)
        page.grid_rowconfigure(2, weight=0)
        page.grid_rowconfigure(3, weight=0)
        page.grid_rowconfigure(4, weight=0)
        page.grid_columnconfigure(0, weight=1)
        page.grid_columnconfigure(1, weight=1)

        # Glyph images
        self.create_glyph_frame(page)

    def create_Info_page(self):
        page2 = ttk.Frame(self.notebook)
        self.notebook.add(page2, text="Info")

        # Center items on the second page
        page2.columnconfigure(0, weight=1)
        page2.rowconfigure(0, weight=1)

        # Add content to the second page (Info)
        info_text = (
            "## Overview\n"
            "The Name-2Glyph-Generator App is a simple graphical user interface (GUI) app\n"
            "using the Tkinter library in Python. Generate a 12-digit hexadecimal code\n"
            "from a user's name and view corresponding glyph images for each digit.\n\n"
            "## Features\n"
            "- Convert any name into a unique 12-digit hexadecimal code.\n"
            "- View and copy the generated code.\n"
            "- Explore glyph images for each digit.\n\n"
            "## How to Use\n"
            '1. Enter a name on the "Convert" page.\n'
            '2. Click "Convert" to generate the code and view glyph images.\n'
            '3. Click "Copy Hex Code" to copy the code.\n'
            '4. Use "Clear" to reset input and output.\n\n'
            "## Creator\n"
            "Created by: Mr Negative\n\n"
            "## Thanks to\n"
            "Special thanks to: Woo for sparking the idea."
        )

        info_label = tk.Label(page2, text=info_text)
        info_label.pack(padx=20, pady=20)

    def enter_key_pressed(self, event):
        self.convert_to_hexadecimal()

    def convert_to_hexadecimal(self):
        name = self.name_entry.get()
        if name:
            hex_representation = self.convert_name_to_hexadecimal(name)
            self.output_text.set(hex_representation)
            self.display_glyph_images(hex_representation)
            self.glyph_frame.grid()  # Show the glyph frame
        else:
            self.output_text.set("Enter a name first.")
            self.clear_glyphs()
            self.glyph_frame.grid_remove()  # Hide the glyph frame

    def convert_name_to_hexadecimal(self, name):
        ascii_values = [ord(char) for char in name]
        hex_representation = "".join([hex(value)[2:].upper() for value in ascii_values])

        if len(hex_representation) > 12:
            hex_representation = hex_representation[:12]
        else:
            hex_representation = hex_representation.zfill(12)

        return hex_representation

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.output_text.set("")
        self.clear_glyphs()
        self.glyph_frame.grid_remove()  # Hide the glyph frame

        # Set focus back to the name entry field
        self.name_entry.focus_set()

    def create_glyph_frame(self, page):
        style = ttk.Style()
        style.configure("Custom.GlyphFrame.TFrame", background="#b133c9")

        self.glyph_frame = ttk.Frame(page, style="Custom.GlyphFrame.TFrame")

        # Apply other configurations and grid settings
        self.glyph_frame.grid(row=5, column=0, columnspan=2, padx=12, pady=320)
        self.glyph_frame.grid_remove()  # Initially hide the frame

    def clear_glyphs(self):
        for widget in self.glyph_frame.winfo_children():
            widget.destroy()

    def display_glyph_images(self, hex_code):
        self.clear_glyphs()

        if hex_code:
            for i, prefix in enumerate(hex_code):
                if prefix in self.glyphs:
                    row = i // 6
                    column = i % 6
                    glyph_image = ttk.Label(self.glyph_frame, image=self.glyphs[prefix])
                    glyph_image.grid(row=row, column=column, padx=2, pady=2)

    def copy_to_clipboard(self):
        hex_value = self.output_text.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(hex_value)
        self.root.update()

    def load_icon(self):
        icon_path = os.path.join(sys._MEIPASS, "data", "icon.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(default=icon_path)
        else:
            print("Icon file not found.")


if __name__ == "__main__":
    root = tk.Tk()

    # Load the icon and create the app
    app = HexCodeGeneratorApp(root)
