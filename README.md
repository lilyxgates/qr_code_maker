Written by Lily Gates  

## Description
Create and save a .png of a QR Code based on user input provided through command-line arguments. The script generates a QR Code from a URL and allows the user to choose color modes (light, dark, custom) for styling.


## Usage
* `<url>`: The endpoint or link you want to encode in the QR Code
* Color modes:
    * `"light"` or `"dark"`: Choose the style of the QR Code (light mode: black on white, dark mode: white on black)
    * `"custom"`: Enter hexadecimal code for colors, will convert to RGB as 'fill_color' and 'back_color' in qrcode module
* `<file_name>`: The name you'd like to save the generated QR Code as (without the .png extension)

## Required Dependencies
* os
* qrcode

