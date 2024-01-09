import time

import serial


class ADC:
    def __init__(self):
        self.serialPort = serial.Serial()

    def init(self, port_name="COM9"):
        self.serialPort = serial.Serial(
            port=port_name, baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
        )

    def get_value(self):
        serial_string = b""  # Used to hold data coming over UART
        while serial_string == b'':
            self.serialPort.write(b"test\n")
            self.serialPort.flush()
            serial_string = self.serialPort.readline()
        return int(serial_string)

    def close_port(self):
        self.serialPort.close()


if __name__ == "__main__":
    converter = ADC()
    converter.init()
    x0 = time.time()
    for i in range(100):
        value = converter.get_value()
        print(f"{i} {time.time() - x0:.2f} {value}")
    converter.close_port()
