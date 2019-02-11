import serial
import serial.tools.list_ports
import datetime

hello_string = "Hello it's now {0}".format(datetime.datetime.now())

def send_text_to_printer(text, com, baud):
    with serial.Serial(port=com, dsrdtr=True, baudrate=baud) as ser:
        ser.write(text.encode())
        ser.write(b"\x1B\x64\x0A")
        ser.write(b"\x1D\x56\x00")

def return_active_coms():
        ports = serial.tools.list_ports.comports()
        return ports

class Baud:
        rates = [
                1200,
                1400,
                4800,
                19200,
                38400,
                57600,
                115200
        ]
