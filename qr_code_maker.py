# QR Code Generator
# Written by Lily Gates

# Description: Create and save a .png of QR Code based on user input command-line arguments.
# Usage: python3 qr_code_maker.py <url>, <"light"|"dark">, <file_name>
# Required Dependencies: os, qrcode

import os
import qrcode

# Initialize QR Code object
qr = qrcode.QRCode(
    version=5,    # Changes the pattern (int 1-40, 40 has most noise)
    box_size=100,  # Size of each box in pixels, will affect dimension size
    border=4,     # Thickness of border (minimum 4)
)

# Prompt for URL input
url = input("Enter endpoint URL for the generated QR Code: ")
qr.add_data(url)

qr.make(fit=True)

# Prompt for light, dark, or custom mode
mode = input("Produce in 'light', 'dark', or 'custom' mode? (Choose 'info' for more): ").strip().lower()

# Provide description option if user selects 'info'
while mode not in ("light", "dark", "custom"):
    if mode == "info":
        print("\nINFORMATION ON COLOR MODES:")
        print("The 'light' mode is BLACK QR code dots on a WHITE background")
        print("The 'dark' mode is WHITE QR code dots on a BLACK background")
        print("The 'custom' mode is CUSTOM COLOR QR code dots on a CUSTOM COLOR background\n")
    else:  # Re-prompt user to re-enter color mode if invalid input
        print("\nERROR: Invalid input\nPlease re-enter your desired color mode.\n")
    mode = input("Produce in 'light', 'dark', or 'custom' mode? (Choose 'info' for more): ").strip().lower()

# Set colors based on mode
if mode == "light":
    fill_color = "black"
    back_color = "white"
elif mode == "dark":
    fill_color = "white"
    back_color = "black"
else:  # Custom mode - convert from hexadecimal to RBG input required
    
    # Prompt 'fill_color' and strip any '#'
    hex_fill_color = input("Enter the fill color (color of the QR code dots) in hexadecimal form: ").strip("#")
    
    """
# TODO: Add troubleshoot option that...
    # Confirms hexidecimal input and the RGB equivalent
    # Re-prompts user if a hexidecimal was NOT inputted (for both 'fill_color' and 'back_color')

    # Troubleshoot whether hexidecimal is valid (6-digits long) or reprompt user
    
    """
    if len(hex_fill_color) != 6:
        print(f"ERROR: '#{hex_fill_color}' is NOT a valid hexidecimal (e.g., #ffffff is white)\n")
        hex_fill_color = input("Enter the fill color (color of the QR code dots) in hexadecimal form: ").strip("#")
    
    if len(hex_fill_color) == 6:
        print(f"Confirming color: #{hex_fill_color}")


    """
    # Confirm 
        # TODO: Ask whether user confirms (Y/N) the color
            # NOTE: accept 'y', 'yes' and 'n' 'no' -- not case-sensitive
                # Throw error message and reprompt user to confirm Y or N if not
        
        confirm_hex_fill = input("PLEASE CONFIRM: 'Yes' or 'No'").lower()
            if confirm_hex_fill == "y" or "yes":
                print(f"CONFIRMED: '#{hex_fill_color}' is the fill color (color of hte QR code dots)\n")
            elif confirm_hex_fill == "n" or "no":
                hex_fill_color = input("Enter the fill color (color of the QR code dots) in hexadecimal form: ").strip("#")

    """

    # Prompt 'back_color' and strip any '#'
    hex_back_color = input("Enter the background color in hexadecimal form: ").strip("#")
   
    # Create tuple from hex input for the 'fill_color' and 'back_color' parameters
    rbg_fill = (int(hex_fill_color[0:2], 16), int(hex_fill_color[2:4], 16), int(hex_fill_color[4:6], 16))
    rbg_back = (int(hex_back_color[0:2], 16), int(hex_back_color[2:4], 16), int(hex_back_color[4:6], 16))

    fill_color = rbg_fill
    back_color = rbg_back

     
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Prompt for file name and save image
file_name = input("Enter the name to save the newly created QR Code as: ")

# Use default name if input is empty or just whitespace
if len(file_name.strip()) == 0:
    file_name = "qr_code"

# Save the image with the filename and mode appended
full_file_name = f"{file_name}_{mode}.png"
img.save(full_file_name)

# Print confirmation statement
print(f"A QR Code for the URL '{url}' has been saved in '{mode}' mode as '{full_file_name}' in the current directory.")
