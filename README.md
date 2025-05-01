Written by Lily Gates  
January 2025

## Description
Create and save a .png of a QR Code based on user input provided through command-line arguments. The script generates a QR Code from a URL and allows the user to choose between light or dark mode for styling.


## Usage
```
python3 qr_code_maker.py <url>, <"light"|"dark">, <file_name>
```
* <url>: The endpoint or link you want to encode in the QR Code
* "light" or "dark": Choose the style of the QR Code (light mode: black on white, dark mode: white on black)
* "custom": Enter hexadecimal code for colors, will convert to RGB as 'fill_color' and 'back_color' in qrcode module
* <file_name>: The name you'd like to save the generated QR Code as (without the .png extension)

Example:
```
python3 qr_code_maker.py https://example.com light example_qr
```

## Required Dependencies
* os
* qrcode

