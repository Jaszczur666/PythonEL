import time

import serial


class ADC:
    def __init__(self):
        self.serialPort = serial.Serial()

    def init(self, port_name="COM11"):
        self.serialPort = serial.Serial(
            port=port_name,
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            timeout=None,
            stopbits=serial.STOPBITS_ONE,
        )
        time.sleep(3) # Give arduino that serves as intermediate time to reset

    def get_value(self):
        serial_string = b""  # Used to hold data coming over UART
        self.serialPort.write(
            b"test\n"
        )  # This actually could be even bare "\n", but experiment showed that
        # sometimes this would break. Sending any short string before \n seems to prevent this.
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
