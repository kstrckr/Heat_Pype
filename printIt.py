import serial
import datetime

hello_string = "Hello it's now {0}".format(datetime.datetime.now())

with serial.Serial(port="COM5", dsrdtr=True, baudrate=38400) as ser:
    ser.write(hello_string.encode())
    ser.write(b"\x1B\x64\x0A")
    ser.write(b"\x1D\x56\x00")
    