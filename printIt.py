import serial
import datetime

hello_string = "Hello it's now {0}".format(datetime.datetime.now())

def send_text_to_printer(text):
    with serial.Serial(port="COM5", dsrdtr=True, baudrate=38400) as ser:
        ser.write(text.encode())
        ser.write(b"\x1B\x64\x0A")
        ser.write(b"\x1D\x56\x00")