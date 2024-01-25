import serial
import time
import device


class Dummy(device.Device):
    def __init__(self):
        self.serialPort = serial.Serial()

    def init(self, port_name="COM10"):
        self.serialPort = serial.Serial(
            port=port_name,
            baudrate=19200,
            bytesize=8,
            timeout=None,
            stopbits=serial.STOPBITS_ONE,
            dsrdtr=False,
        )
        time.sleep(3)  # Arduino resets on connection, give it time to restart

    def parse(self, command):
        self.serialPort.write(command)
        print(f"Written {command}")
        self.serialPort.flush()
        time.sleep(0.01)
        response = self.serialPort.readline()
        print(response)
        return None


if __name__ == "__main__":
    slow_device = Dummy()
    slow_device.init()
    for i in range(12):
        print(i)
        slow_device.parse(b"Dubzgo!")
