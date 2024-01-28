import time

import serial

import device

"""
This class is a driver for dummy device, which echoes everything sent its way after random delay. 
This is one of the vital tests as some operations particularly for monochromators can take quite a lot of time,
and it's important for experimental loop to assure that we wait for the end of operation before starting next one

"""


class Dummy(device.Device):
    def __init__(self):
        self.serialPort = serial.Serial()

    def init(self, port_name="COM10"):
        self.serialPort = serial.Serial(
            port=None,
            baudrate=19200,
            bytesize=8,
            timeout=None,
            stopbits=serial.STOPBITS_ONE,
            dsrdtr=False,
        )
        self.serialPort.port = port_name
        self.serialPort.dtr = False
        self.serialPort.open()
        # time.sleep(3)  # Arduino resets on connection, give it time to restart

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
        slow_device.parse(b"Testing")
