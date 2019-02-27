#python -m serial.tools.list_ports

import argparse

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
                9600,
                19200,
                38400,
                57600,
                115200
        ]

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("text", help="text to print")
        parser.add_argument("com", help="com poart to use, formatted as comX")
        parser.add_argument("baud", help="baud rate to use", type=int)

        args = parser.parse_args()
        
        if args.baud in Baud.rates:
                print("Printing \"{}\" on {} at {} baud".format(args.text, args.com, args.baud))
                send_text_to_printer(args.text, args.com, args.baud)