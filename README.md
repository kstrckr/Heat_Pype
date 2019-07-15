#Heat Pype
A gui app for processing and printing images on serial Epson thermal printers

![Alt text](/screenshots/Capture.PNG "Heat Pype UI Screenshot")

1. Activate your virtual environment of choice, preferably https://docs.python.org/3/library/venv.html
2. Install dependencies via `pip install -r requirements.txt`
3. Run the program `python heat_pype.py`
4. From the UI, click `Select Image`
..* The source image is previewed on the left, with the output displayed on the right
..* Click and drag on the source image to crop the output, the result will be displayed in real time
..* Click and drag again to select a new crop
..* Right Click and drag to move the crop around without changing its size
..* *Aspect ratio is not maintained, and strange ratio crops can be used for creative effect
5. Set the Com port and Baud Rate from the dropdowns in the top-left corner 
..* Com port options should be self populating, if you don't see any listed make sure your USB to Serial adapter is operational or your serial port is connected properly
6. Click print to send the dithered image data to the printer, depending on the baud rate used this may take a moment.



`Clear` and `File -> Open Image` have not yet been implemented