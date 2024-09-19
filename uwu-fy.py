# Import libraries & modules
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from PIL import Image, ImageTk
import random
import os

# Colors
baby_pink = "#ffe1f0"
ashy_blue_purple = "#949ac4" 
dark_purple = "#616ca8"
ashy_purple = "#8180b4"
off_white = "#f6f9f6"

# Modify script to load the font
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Function to uwu-fy text and add kaomojis
def uwu_fy(text):
    text = text.lower()
    
    # Replace characters to uwu-fy
    text = text.replace('r', 'w').replace('l', 'w')
    text = text.replace('s', 'sh')
    text = text.replace('th', 'd')
    text = text.replace('o', 'yo')
    text = text.replace('u', 'yu')
    
    # Replace specific words
    text = text.replace('you', 'yuwu').replace('my', 'mew').replace('no', 'nuu')
    
    # Punctuation replacements
    punctuation_replacements = {
        '.': '~~',
        ',': '~',
        '!': '!!',
        '?': '??',
    }
    
    # Split text into characters
    processed_text = []
    for char in text:
        # Check if the character is punctuation
        if char in punctuation_replacements:
            # Randomly replace punctuation; 60% chance
            if random.random() > 0.4:
                processed_text.append(punctuation_replacements[char])
            else:
                processed_text.append(char)
        else:
            processed_text.append(char)
            
    # Join back to single string
    text = ''.join(processed_text)
    
    # Split the words for further processing
    words = text.split()
    
    # Process each word to add stuttering
    uwu_words = []
    for word in words:
        # Randomly stutter word; 15% chance
        if random.random() > 0.85:
            word = f"{word[0]}={word[0]}-{word}"
        # For words longer than 10 letters; chance 40%
        elif len(word) > 10 and random.random() > 0.6:
            word = f"{word[0]}-{word[0]}-{word}"
            
        uwu_words.append(word)
        
    # Join words back together
    text = ' '.join(uwu_words)

    # Add random kaomoji
    kaomojis = ['(≧◡≦)', '(•ω•)', '(UwU)', '(｡♥‿♥｡)', '(✿◠‿◠)', '(⁄ ⁄•⁄ω⁄•⁄ ⁄)', '(。UωU。)']
    text += " " + random.choice(kaomojis)
    
    return text

# Function to get the input, uwu-fy it, and display it
def process_text():
    # Retrieve text from input; "1.0" refers to position of the text box, tk.END indicates the end of the text box
    input_text = input_box.get("1.0", tk.END)
    # Call the uwu_fy function and pass input_text as an argument
    uwu_text = uwu_fy(input_text)
    # Temporarily enables output_box by changing its state to normal, allowing for modifications
    output_box.config(state = tk.NORMAL)
    # Clear existing text, making sure it's empty before inserting new text
    output_box.delete("1.0", tk.END)
    # Insert the uwu-fied text
    output_box.insert(tk.END, uwu_text)
    # After inserting text, disable output_box
    output_box.config(state = tk.DISABLED)

# Function to center the window
def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate position x, y for center alignment
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    root.geometry(f'{width}x{height}+{x}+{y}')

# Main window
root = tk.Tk()
root.title("UWU-fier")
root.configure(bg = "#cdb4db")

# Register font
font_path = resource_path("soda_cream.otf")
root.tk.call("font", "create", "MyCustomFont", "-family", font_path, "-weight", "normal")

# Use the custom font
soda_cream = tkFont.Font(family = "SodaCream", size = 16)

# Load GIF frames using Pillow
gif_file = resource_path("march.gif")
gif_image = Image.open(gif_file)
gif_width, gif_height = gif_image.size
photoimage_objects = []

try:
    while True:
        photoimage_objects.append(ImageTk.PhotoImage(gif_image.copy()))
        gif_image.seek(gif_image.tell() + 1)
except EOFError:
    pass

# Set window size
additional_height = 360
window_width = gif_width
window_height = gif_height + additional_height
center_window(root, window_width, window_height)

# Create header
def create_header():
    header_text = "UwU Text Generatowu (｡♥‿♥｡)"
    header_label = tk.Label(root, text = header_text, fg = dark_purple, bg = "#cdb4db", font=("Comic Sans MS", 30, "bold"))
    header_label.pack(pady = (5, 15))
create_header()

# Input box
input_frame = ttk.Frame(root)
input_frame.pack()
input_box = tk.Text(root, height = 5, width = 60, bg = baby_pink, fg = ashy_purple, font = soda_cream, relief = "flat", pady = 10, padx = 10)
input_box.pack()

# UWU-fy button
uwu_button = tk.Button(root, text = "UWU-fy! (•ω•)", command = process_text, fg =  off_white, bg = ashy_blue_purple, font=("Segoe UI", 12), relief = "flat", borderwidth = 5, padx = 10, pady = 5, highlightthickness=0, bd = 0)
uwu_button.pack(pady = 13)

# Output box
output_frame = ttk.Frame(root)
output_frame.pack()
output_box = tk.Text(root, height = 5, width = 60, bg = baby_pink, fg = ashy_purple, font=soda_cream, relief = "flat", pady = 10, padx = 10)
output_box.pack()

# Label to display the GIF
gif_label = tk.Label(root, bg = baby_pink)
gif_label.pack(fill = "both", pady = (10, 0))

# Function for animation start
def animation(current_frame = 0):
    global loop
    image = photoimage_objects[current_frame]
    gif_label.configure(image = image)
    current_frame = (current_frame + 1) % len(photoimage_objects)
    loop = root.after(50, lambda: animation(current_frame))
animation()

# Run
root.mainloop()

