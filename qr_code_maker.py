# QR Code Generator
# Written by Lily Gates
# January 2025

# Description: Create and Save a .png of QR Code Based on User Input Command-Line Arguments.
# Usage: python3 qr_code_maker.py <url>, <"light"|"dark">, <file_name>
# Required Dependencies: os, qrcode

import os
import qrcode

qr = qrcode.QRCode(
    version=1,  # Size of QR Code
    box_size=10, # Number of pixels each “box” of the QR code is
    border=4,
)

# URL input
url = input("Enter endpoint URL for the generated QR Code: ")
qr.add_data(url)

qr.make(fit=True)

# Customize light/dark mode based on command-line argument
mode_input = input("Produce in 'light' or 'dark' mode? ").lower()
mode = mode_input.lower()

while mode != "light" and mode != "dark": 
    mode = input("Produce in 'light' or 'dark' mode? ").lower()

if mode == "light":
    img = qr.make_image(fill_color="black", back_color="white")
elif mode == "dark":
    img = qr.make_image(fill_color="white", back_color="black")

# Save as .png in the current directory based on command-line argument
file_name = input("Enter the name to save the newly created QR Code as: ")
img.save(f"{file_name}.png")

# Print confirmation statement
print(f"A QR Code for the URL '{url}' has been saved in '{mode}' mode as '{file_name}.png' in the current directory.")