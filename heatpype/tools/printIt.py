import serial
import serial.tools.list_ports
import datetime

hello_string = "Hello it's now {0}".format(datetime.datetime.now())

class EpsonCommands():

    @classmethod
    def send_text_to_printer(self, text, com, baud):
        with serial.Serial(port=com, dsrdtr=True, baudrate=baud) as ser:
            ser.write(text.encode())
            ser.write(b"\x1B\x64\x0A")
            ser.write(b"\x1D\x56\x00")

    @classmethod
    def print_raster_data(self, width, height, raster_data_bytes, com, baud):
        with serial.Serial(port=com, dsrdtr=True, baudrate=baud) as ser:
            #initialize printer: ESC @
            ser.write(b"\x1B\x40")

            #set dpi to 380
            # ser.write(b"\x1d\x28\x4c\x04\x00\x30\x31\x33\x33")

            #send raster data to buffer: GS ( L   /   GS 8 L   <Function 112>
            raster_command = self.programatic_raster_printing(width, height, raster_data_bytes)
            ser.write(raster_command)

            #print the data in buffer: GS ( L   <Function 50>
            ser.write(b"\x1d\x28\x4c\x02\x00\x30\x32")

            #print and feed n lines ESC d
            # ser.write(b"\x1b\x64\x0a")

            #cut
            # ser.write(b"\x1d\x56\x00")
            
            #initialize printer: ESC @
            # ser.write(b"\x1B\x40")
            #Select cut mode and cut paper GS V
            ser.write(b"\x1D\x56\x41\x64")
    
    @classmethod
    def get_byte_length(self, raster_data_bytes):
        byte_length = len(raster_data_bytes) + 10
        print(byte_length)
        pL = int(byte_length % 256)
        pH = int(byte_length / 256)
        print(pL, pH)
        return (bytes([pL]), bytes([pH]))


    @classmethod
    def programatic_raster_printing(self, width, height, raster_data_bytes):

        command = bytes.fromhex('1d') + bytes.fromhex('28') + bytes.fromhex('4c')
        pL, pH = self.get_byte_length(raster_data_bytes)
        m = bytes.fromhex('30')
        fn = bytes.fromhex('70')
        a = bytes([48])
        xScale = bytes([1])
        yScale = bytes([1])
        c = bytes([49])
        xL = bytes([int(width % 256)])
        xH = bytes([int(width / 256)])
        yL = bytes([int(height % 256)])
        yH = bytes([int(height / 256)])

        full_command = b"".join([command, pL, pH, m, fn, a, xScale, yScale, c, xL, xH, yL, yH])

        full_raster_tx = b"".join([full_command, raster_data_bytes])

        # print(full_raster_tx)

        return full_raster_tx