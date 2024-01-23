import time

import serial


class Boxcar:
    def __init__(self):
        self.serialPort = serial.Serial()

    def init(self, port_name="COM5"):
        self.serialPort = serial.Serial(
            port=port_name,
            baudrate=19200,
            bytesize=8,
            timeout=2,
            stopbits=serial.STOPBITS_ONE,
            )
        self.serialPort.write(b"W0\r")
    def get_value(self):
        serial_string = b""  # Used to hold data coming over UART
        while (
            serial_string == b""
        ):  
            self.serialPort.write(
                b"?1\r"
            )  
            self.serialPort.flush()
            serial_string = self.serialPort.read_until(b"\r")
            print(serial_string)
        return float(serial_string)

    def close_port(self):
        self.serialPort.close()

        
if __name__ == "__main__":
    srsbox = Boxcar()
    srsbox.init()
    x0 = time.time()
    for i in range(1000):
        value = srsbox.get_value()
        print(f"{i} {time.time() - x0:.2f} {value}")
    srsbox.close_port()
